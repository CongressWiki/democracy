import React from 'react';
import {initializeApollo, addApolloState, withApollo} from '@lib/withApollo';
import {gql, useQuery, NetworkStatus} from '@apollo/client';
import Layout from '@components/Layout/Layout';
import BillCanvas from '@components/BillCanvas/BillCanvas';
import CircularProgress from '@components/CircularProgress/CircularProgress';
import Error from 'next/error';
import {Button} from '@material-ui/core';

const GET_LATEST_BILLS = gql`
  query getLatestBills($limit: Int!, $offset: Int!) {
    bills(order_by: { updated_at: desc }, limit: $limit, offset: $offset) {
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
    bills_aggregate {
      aggregate {
        count
      }
    }
  }
`;

export const getStaticProps = async ({params}, ctx) => {
	const apolloClient = initializeApollo(ctx);

	await apolloClient.query({
		query: GET_LATEST_BILLS,
		variables: {
			offset: 0,
			limit: 3
		}
	});

	return addApolloState(apolloClient, {
		props: {},
		revalidate: 1
	});
};

const Bills = () => {
	const {loading, error, data, fetchMore, networkStatus} = useQuery(GET_LATEST_BILLS,
		{
			variables: {
				offset: 0,
				limit: 3
			},
			// Setting this value to true will make the component rerender when
			// the "networkStatus" changes, so we are able to know if it is fetching
			// more data
			notifyOnNetworkStatusChange: true
		});

	const loadingMoreBills = networkStatus === NetworkStatus.fetchMore;
	const {bills, bills_aggregate} = data;
	const areMoreBills = bills.length < bills_aggregate.count;

	const loadMoreBills = () => {
		(fetchMore as any)({
			variables: {
				offset: bills.length
			}
		});
	};

	if (loading || loadingMoreBills) {
		return (
			<Layout>
				<main>
					<CircularProgress/>
				</main>
			</Layout>
		);
	}

	if (error) {
		console.error(JSON.stringify(error, null, 2));
		return (
			<Error statusCode={400} title="GraphQL error"/>
		);
	}

	return (
		<Layout>
			<Button
				disabled={loadingMoreBills} onClick={() => {
					loadMoreBills();
				}}
			>{loadingMoreBills ? 'Loading...' : 'Show More'}
			</Button>
			<main>
				<BillCanvas bills={bills || []}/>
			</main>
		</Layout>
	);
};

// Export default Bills;
export default withApollo(Bills);
