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
			order_by: { updated_at: desc }
		) {
			id
			introduced_at
			official_title
			popular_title
			short_title
			sponsor
			status
			status_at
			subjects
			subjects_top_term
			summary
			titles
			updated_at
			history
			enacted_as
			cosponsors
			committees
			committee_reports
			amendments
			actions
		}
	}
`;

const BillCanvas = () => {
	const {loading, error, data} = useQuery(GET_LATEST_BILLS);

	if (loading) {
		return <CircularProgress/>;
	}

	if (error) {
		return <span>Error {JSON.stringify(error)}</span>;
	}

	if (data) {
		return (
			<Grid container spacing={3}>
				{data.bills.map(billData => (
					<Grid key={billData?.id} item xs={12}>
						<Bill
							id={billData?.id}
							title={billData?.official_title}
							summary={billData?.summary?.text}
						/>
					</Grid>
				))}
			</Grid>
		);
	}
};

export default BillCanvas;
