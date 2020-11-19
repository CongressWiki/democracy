import {ApolloClient} from 'apollo-client';
import {HttpLink} from 'apollo-link-http';
import {InMemoryCache} from 'apollo-cache-inmemory';
import {SubscriptionClient} from 'subscriptions-transport-ws';
import {WebSocketLink} from 'apollo-link-ws';
import fetch from 'isomorphic-unfetch';
// Import {onError} from 'apollo-link-error';

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
		uri: 'http://localhost:8080/v1/graphql',
		headers: {
			'x-hasura-admin-secret': 'hasurapassword'
		}, // Auth token is fetched on the server side
		fetch
	});
	return httpLink;
};

const createWSLink = () => {
	return new WebSocketLink(
		new SubscriptionClient('ws://localhost:8080/v1/graphql', {
			lazy: true,
			reconnect: true,
			connectionParams: async () => {
				// Await requestAccessToken() // happens on the client
				return {
					headers: {
						'x-hasura-admin-secret': 'hasurapassword'
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
