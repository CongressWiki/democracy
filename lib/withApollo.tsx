import React, {useMemo} from 'react';

import {ApolloClient, HttpLink, InMemoryCache, ApolloProvider} from '@apollo/client';
import {concatPagination} from '@apollo/client/utilities';
import merge from 'deepmerge';
import isEqual from 'lodash/isEqual';
import type {NormalizedCacheObject} from '@apollo/client';

export const APOLLO_STATE_PROP_NAME = '__APOLLO_STATE__';

let apolloClient: ApolloClient<NormalizedCacheObject>;

function createApolloClient() {
	return new ApolloClient({
		ssrMode: typeof window === 'undefined',
		link: new HttpLink({
			uri: 'https://usacounts.com/v1/graphql', // Server URL (must be absolute)
			credentials: 'same-origin', // Additional fetch() options like `credentials` or `headers`
			headers: {
				'x-hasura-role': 'anonymous-website-user'
			},
			fetch
		}),
		cache: new InMemoryCache({
			typePolicies: {
				Query: {
					fields: {
						bills: concatPagination()
					}
				}
			}
		})
	});
}

export function initializeApollo(initialState: NormalizedCacheObject = null) {
	const _apolloClient: ApolloClient<NormalizedCacheObject> = apolloClient ?? createApolloClient();

	// If your page has Next.js data fetching methods that use Apollo Client, the initial state
	// gets hydrated here
	if (initialState) {
		// Get existing cache, loaded during client side data fetching
		const existingCache = _apolloClient.extract();

		// Merge the existing cache into data passed from getStaticProps/getServerSideProps
		const data = merge(initialState, existingCache, {
			// Combine arrays using object equality (like in sets)
			arrayMerge: (destinationArray, sourceArray) => [
				...sourceArray,
				...destinationArray.filter(d =>
					sourceArray.every(s => !isEqual(d, s))
				)
			]
		});

		// Restore the cache with the merged data
		_apolloClient.cache.restore(data);
	}

	// For SSG and SSR always create a new Apollo Client
	if (typeof window === 'undefined') {
		return _apolloClient;
	}

	// Create the Apollo Client once in the client
	if (!apolloClient) {
		apolloClient = _apolloClient;
	}

	return _apolloClient;
}

export function addApolloState(client: ApolloClient<NormalizedCacheObject>, pageProps) {
	if (pageProps?.props) {
		pageProps.props[APOLLO_STATE_PROP_NAME] = client.cache.extract();
	}

	return pageProps;
}

function useApollo(pageProps) {
	const state = pageProps[APOLLO_STATE_PROP_NAME];
	const store = useMemo(() => initializeApollo(state), [state]);
	return store;
}

export function withApollo(PageComponent) {
	const WithApollo = ({
		apolloStaticCache,
		...pageProps
	}) => {
		const client = useApollo(pageProps);
		// HERE WE USE THE PASSED CACHE
		// const client = initializeApollo(apolloStaticCache);
		// And here we have the initialized client 🙂
		return (
			<ApolloProvider client={client}>
				<PageComponent {...pageProps}/>
			</ApolloProvider>
		);
	};

	// If you also use it for SSR
	if (PageComponent.getInitialProps) {
		WithApollo.getInitialProps = async ctx => {
			// Run wrapped getInitialProps methods
			let pageProps = {};
			if (PageComponent.getInitialProps) {
				pageProps = await PageComponent.getInitialProps(ctx);
			}

			return pageProps;
		};
	}

	// Set the correct displayName in development
	if (process.env.NODE_ENV !== 'production') {
		const displayName =
      PageComponent.displayName || PageComponent.name || 'Component';

		WithApollo.displayName = `withApollo(${displayName as string})`;
	}

	return WithApollo;
}
