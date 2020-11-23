import Paper from '@material-ui/core/Paper';
import PropTypes from 'prop-types';
import React from 'react';
import {makeStyles} from '@material-ui/core/styles';

export interface BillProps {
	/**
   * Category of bill
   */
	subjects_top_term: string;
	/**
   * Bill title
   */
	official_title: string;
	/**
   * Summary of bill
   */
	summary: string;
}

const useStyles = makeStyles({
	root: {
		// Position: 'absolute',
		display: 'inline-block',
		background: 'linear-gradient(45deg, #2979ff 30%, #f44336 90%)',
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

export const Bill = props => {
	const classes = useStyles();

	return (
		<Paper elevation={3} className={classes.root}>
			<h3>{props.subjects_top_term}</h3>
			<b>{props.official_title}</b>
			<p>{props.summary}</p>
		</Paper>
	);
};

Bill.propTypes = {
	subjects_top_term: PropTypes.string.isRequired,
	official_title: PropTypes.string.isRequired,
	summary: PropTypes.string.isRequired
};
