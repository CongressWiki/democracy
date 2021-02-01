module.exports = {
	serverRuntimeConfig: {
		// Will only be available on the server side
		NEXT_PUBLIC_GRAPHQL_ENDPOINT: process.env.NEXT_PUBLIC_GRAPHQL_ENDPOINT,
		NEXT_PUBLIC_HASURA_GRAPHQL_ADMIN_SECRET: process.env.NEXT_PUBLIC_HASURA_GRAPHQL_ADMIN_SECRET
	},
	publicRuntimeConfig: {
		// Will be available on both server and client
		// staticFolder: '/static'
	}
};

