import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { SubscriptionClient } from 'subscriptions-transport-ws'
import { WebSocketLink } from 'apollo-link-ws'
import fetch from 'isomorphic-unfetch'
import { onError } from 'apollo-link-error'

let accessToken = null

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

const createHttpLink = (headers) => {
  const httpLink = new HttpLink({
    uri: `http://localhost:8080/v1/graphql`,
    headers: {
      'x-hasura-admin-secret': 'hasurapassword',
    }, // auth token is fetched on the server side
    fetch,
  })
  return httpLink
}

const createWSLink = () => {
  return new WebSocketLink(
    new SubscriptionClient(`ws://localhost:8080/v1/graphql`, {
      lazy: true,
      reconnect: true,
      connectionParams: async () => {
        // await requestAccessToken() // happens on the client
        return {
          headers: {
            'x-hasura-admin-secret': 'hasurapassword',
          },
        }
      },
    })
  )
}

export default function createApolloClient(initialState, headers) {
  const ssrMode = typeof window === 'undefined'
  let link
  if (ssrMode) {
    link = createHttpLink(headers) // executed on server
  } else {
    link = createWSLink() // executed on client
  }
  return new ApolloClient({
    ssrMode,
    link,
    cache: new InMemoryCache().restore(initialState),
  })
}
