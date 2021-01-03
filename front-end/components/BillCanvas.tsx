import {Bill} from './Bill';
import CircularProgress from '@material-ui/core/CircularProgress';
import Grid from '@material-ui/core/Grid';
import React from 'react';
import gql from 'graphql-tag';
import {useQuery} from '@apollo/react-hooks';

const GET_LATEST_BILLS = gql`
	query getLatestBills {
		bills(
			limit: 3
			order_by: { status_at: desc }
		) {
			id
			type
			by_request
			number
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

const BillCanvas = () => {
	const {loading, error, data} = useQuery(GET_LATEST_BILLS);

	if (loading) {
		return <CircularProgress/>;
	}

	if (error) {
		return <span>Error {JSON.stringify(error, null, 2)}</span>;
	}

	if (data) {
		return (
			<Grid container spacing={3}>
				{data.bills.map(billData => (
					<Grid key={billData?.id} item xs={12}>
						<Bill
							id={billData?.id}
							title={billData?.title}
							summary={JSON.stringify(billData, null, 2)}
						/>
					</Grid>
				))}
			</Grid>
		);
	}
};

export default BillCanvas;
