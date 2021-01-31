import React from 'react';
import gql from 'graphql-tag';
import {withApollo} from '@libs/with-apollo';
import {useQuery} from '@apollo/react-hooks';
import Layout from '@components/Layout/Layout';
import CircularProgress from '@components/CircularProgress/CircularProgress';
import CongressGrid from '@components/CongressGrid/CongressGrid';

const GET_ELECTED_OFFICIALS = gql`
  query getElectedOfficials {
    elected_officials {
      id
      political_party_id
      member_id
      is_active
      position
      state
    }
  }
`;

const Congress = () => {
	const {loading, error, data} = useQuery(GET_ELECTED_OFFICIALS);

	if (loading) {
		return (
			<Layout>
				<CircularProgress/>
			</Layout>
		);
	}

	if (error) {
		return (
			<Layout>
				<span>Error {JSON.stringify(error, null, 2)}</span>
			</Layout>
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
