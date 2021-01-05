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

const BillCanvas = () => {
	const {loading, error, data} = useQuery(GET_LATEST_BILLS);

	if (loading) {
    return (
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <CircularProgress />
        </Grid>
      </Grid>
    )
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
							id={`${billData.type}.${billData.number}`.toUpperCase()}
							title={billData?.title}
							summary={billData?.summary}
						/>
					</Grid>
				))}
			</Grid>
		);
	}
};

export default BillCanvas;
