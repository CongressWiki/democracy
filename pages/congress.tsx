import React from 'react';
import gql from 'graphql-tag';
import {withApollo} from '@lib/withApollo';
import {useQuery} from '@apollo/react-hooks';
import Layout from '@components/Layout/Layout';
import CircularProgress from '@components/CircularProgress/CircularProgress';
import CongressGrid from '@components/CongressGrid/CongressGrid';
import Error from 'next/error';

const GET_ELECTED_OFFICIALS = gql`
  query getElectedOfficials {
    elected_officials(where: {is_active: {_eq: true}}) {
      id
      preferred_name
      political_party
      type
      state
    }
  }
`;

const Congress = () => {
	const {loading, error, data} = useQuery(GET_ELECTED_OFFICIALS);

	if (loading) {
		return (
			<Layout>
				<main>
					<CircularProgress/>
				</main>
			</Layout>
		);
	}

	if (error) {
		console.error(error);
		return (
			<Error statusCode={400} title="GraphQL error"/>
		);
	}

	if (data.elected_officials) {
		return (
			<Layout>
				<main>
					<CongressGrid electedOfficials={data.elected_officials}/>
				</main>
			</Layout>
		);
	}
};

export default withApollo({ssr: true})(Congress);
