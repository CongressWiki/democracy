import React from 'react';
import gql from 'graphql-tag';
import {withApollo} from '@libs/with-apollo';
import {useQuery} from '@apollo/react-hooks';
import Layout from '@components/Layout/Layout';
import BillCanvas from '@components/BillCanvas/BillCanvas';
import CircularProgress from '@components/CircularProgress/CircularProgress';

const GET_LATEST_BILLS = gql`
  query getLatestBills {
    bills(limit: 15, order_by: { updated_at: desc }) {
      id
      type
      number
      by_request
      subject
      introduced_at
      updated_at
      title
      summary
      status
      status_at
      congress
      actions
      sponsor
    }
  }
`;

const Bills = () => {
	const {loading, error, data} = useQuery(GET_LATEST_BILLS);

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
		return (
			<Layout>
				<main>
					<span>Error {JSON.stringify(error, null, 2)}</span>
				</main>
			</Layout>
		);
	}

	if (data.bills) {
		return (
			<Layout>
				<main>
					<BillCanvas bills={data.bills}/>
				</main>
			</Layout>
		);
	}
};

export default withApollo({ssr: true})(Bills);
