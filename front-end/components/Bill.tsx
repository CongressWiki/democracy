import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import PropTypes from 'prop-types';
import React from 'react';
import Skeleton from '@material-ui/lab/Skeleton';
import {makeStyles} from '@material-ui/core/styles';

export interface BillProps {
	id: string;

	/**
   * Bill title
   */
	title: string;
	/**
   * Summary of bill
   */
	summary: string;
}

const useStyles = makeStyles(theme => ({
	paper: {
		width: '67%',
		margin: 'auto',
		borderRadius: 1,
		padding: theme.spacing(2),
		background: 'rgba(251, 251, 248)',
		boxShadow: '0 3px 5px 2px rgba(0, 0, 0, .3)'
	},
	header: {
		margin: 0,
		padding: 0,
		justifyContent: 'flex-start'
	}
}));

export const Bill = props => {
	const classes = useStyles();

	return (
		<Paper elevation={3} className={classes.paper}>
			<Grid container spacing={1}>
				<Grid item xs className={classes.header}>
					{props.id ? <p>{props.id}</p> : <Skeleton variant="text" animation="wave" height={22} width="10%" style={{marginBottom: 30}}/>}
				</Grid>
				<Grid item xs={12}>
					{props.title ?
						<h3>{props.title}</h3> :
						<Skeleton variant="text" animation="wave" height={22} width="80%" style={{marginBottom: 30}}/>}
				</Grid>
				<Grid item xs={12}>
					{props.summary ? <p>{props.summary}</p> : <Skeleton variant="text" animation="wave" height={18}/>}
				</Grid>
			</Grid>
		</Paper>
	);
};

Bill.propTypes = {
	id: PropTypes.string,
	title: PropTypes.string,
	summary: PropTypes.string
};
