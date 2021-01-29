import Layout from '@components/Layout/Layout';
import React from 'react';
import {withApollo} from '@libs/with-apollo';
import CircularProgress from '@material-ui/core/CircularProgress';
import gql from 'graphql-tag';
import {useQuery} from '@apollo/react-hooks';
import BillCanvas from '@components/BillCanvas/BillCanvas';

const GET_LATEST_BILLS = gql`
  query getLatestBills {
    bills(limit: 3, order_by: { updated_at: desc }) {
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

	if (data.bills) {
		return (
			<Layout>
				<BillCanvas bills={data.bills}/>
			</Layout>
		);
	}
};

export default withApollo()(Bills);
