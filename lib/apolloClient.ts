import fetch from 'isomorphic-unfetch';
import {ApolloClient} from 'apollo-client';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {HttpLink} from 'apollo-link-http';
// Import {onError} from 'apollo-link-error';
import {WebSocketLink} from 'apollo-link-ws';
import {SubscriptionClient} from 'subscriptions-transport-ws';

const HTTPS_GRAPHQL_ENDPOINT = process.env.GRAPHQL_ENDPOINT || '';
// Console.log({HTTPS_GRAPHQL_ENDPOINT});
const WSS_GRAPHQL_ENDPOINT = HTTPS_GRAPHQL_ENDPOINT.replace('https', 'wss');
const HASURA_GRAPHQL_ADMIN_SECRET = process.env.GRAPHQL_SECRET;

// Const accessToken = null;
// Const requestAccessToken = async () => {
// 	if (accessToken) {
// 		return;
// 	}

// 	const response = await fetch(`${process.env.APP_HOST}/api/session`);
// 	if (response.ok) {
// 		const json = await response.json();
// 		accessToken = json.accessToken;
// 	} else {
// 		accessToken = 'public';
// 	}
// };

// // Remove cached token on 401 from the server
// const resetTokenLink = onError(({networkError}) => {
// 	if (networkError && networkError.name === 'ServerError' && networkError.statusCode === 401) {
// 		accessToken = null;
// 	}
// });

const createHttpLink = () => {
	const httpLink = new HttpLink({
		uri: `${HTTPS_GRAPHQL_ENDPOINT}/v1/graphql`,
		credentials: 'include',
		headers: {
			'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET,
			'x-hasura-role': 'anonymous-website-user'
		}, // Auth token is fetched on the server side
		fetch
	});
	return httpLink;
};

const createWSLink = () => {
	return new WebSocketLink(
		new SubscriptionClient(`${WSS_GRAPHQL_ENDPOINT}/v1/graphql`, {
			lazy: true,
			reconnect: true,
			connectionParams: () => {
				// Await requestAccessToken() // happens on the client
				return {
					headers: {
						'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET,
						'x-hasura-role': 'anonymous-website-user'
					}
				};
			}
		})
	);
};

export default function createApolloClient(initialState) {
	const ssrMode = typeof window === 'undefined';
	const link = ssrMode ? createHttpLink() : createWSLink();

	return new ApolloClient({
		ssrMode,
		link,
		cache: new InMemoryCache().restore(initialState)
	});
}
