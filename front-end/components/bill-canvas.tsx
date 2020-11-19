import React, {Fragment, useEffect, useState} from 'react';
import {useApolloClient, useSubscription} from '@apollo/react-hooks';

import Box from '@material-ui/core/Box';
import Container from '@material-ui/core/Container';
import gql from 'graphql-tag';
import {makeStyles} from '@material-ui/core/styles';

const useStyles = makeStyles({
	root: {
		// Position: 'absolute',
		display: 'inline-block',
		background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
		border: 1,
		borderRadius: 3,
		boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
		color: 'white',
		// Height: '100%',
		padding: '30px',
		top: '-10px',
		margin: '30px 0 30px 0'
	}
});

const Bill = props => {
	const [state, setState] = useState({
		bills: []
	});

	useEffect(
		() => {
			setState(previousState => {
				return {...previousState, bills: props.bills};
			});
		},
		[]
	);

	const classes = useStyles();

	return (
		<Container style={{position: 'relative', width: '100%', height: '100%'}}>
			{state.bills.map((bill, index) => {
				return (
					<Box key={index} color="text.primary" className={classes.root}>
						<p>{bill.subjects_top_term}</p>
						<b>{bill.official_title}</b>
						<p>{bill?.summary?.text}</p>
					</Box>
				);
			})}
		</Container>
	);
};

// Run a subscription to get the latest Proposal
const GET_LATEST_BILLS = gql`
  subscription getLatestBills {
    bills(
      limit: 10
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
	const {loading, error, data} = useSubscription(GET_LATEST_BILLS);
	if (loading) {
		return <span>Loading...</span>;
	}

	if (error) {
		return <span>Error {JSON.stringify(error)}</span>;
	}

	if (data) {
		return (
			<Bill bills={data?.bills?.length > 0 ? data.bills : null}/>
		);
	}
};

export default BillCanvas;
