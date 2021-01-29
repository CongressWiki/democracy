import {ApolloClient} from 'apollo-client';
import {HttpLink} from 'apollo-link-http';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {SubscriptionClient} from 'subscriptions-transport-ws';
import {WebSocketLink} from 'apollo-link-ws';
import fetch from 'isomorphic-unfetch';
// Import {onError} from 'apollo-link-error';

const GRAPHQL_ENDPOINT = process.env.NEXT_PUBLIC_GRAPHQL_ENDPOINT || '';
const HASURA_GRAPHQL_ADMIN_SECRET = process.env.NEXT_PUBLIC_HASURA_GRAPHQL_ADMIN_SECRET || '';

console.log({GRAPHQL_ENDPOINT})

const HTTPS_GRAPHQL_ENDPOINT = GRAPHQL_ENDPOINT;
const WSS_GRAPHQL_ENDPOINT = GRAPHQL_ENDPOINT.replace('https', 'wss');

// Let accessToken = null

// const requestAccessToken = async () => {
//   if (accessToken) return
//   const res = await fetch(`http://${process.env.NEXT_JS_URL}/api/session`)
//   if (res.ok) {
//     const json = await res.json()
//     accessToken = json.accessToken
//   } else {
//     accessToken = 'public'
//   }
// }

// // remove cached token on 401 from the server
// const resetTokenLink = onError(({ networkError }) => {
//   if (
//     networkError &&
//     networkError.name === 'ServerError' &&
//     networkError.statusCode === 401
//   ) {
//     accessToken = null
//   }
// })

const createHttpLink = () => {
	const httpLink = new HttpLink({
		uri: `${HTTPS_GRAPHQL_ENDPOINT}/v1/graphql`,
		headers: {
			'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
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
			connectionParams: async () => {
				// Await requestAccessToken() // happens on the client
				return {
					headers: {
						'x-hasura-admin-secret': HASURA_GRAPHQL_ADMIN_SECRET
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