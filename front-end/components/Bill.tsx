import {makeStyles, useTheme} from '@material-ui/core/styles';

import Divider from '@material-ui/core/Divider';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import PropTypes from 'prop-types';
import React from 'react';
import Skeleton from '@material-ui/lab/Skeleton';
import Typography from '@material-ui/core/Typography';

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
	},
	indent: props => ({
		textIndent: '-3em',
		paddingLeft: '3em'
		// Display: 'inline-flex'
		// '&:(first-line)': {
		// 	textIndent: 0
		// }
	})
}));

export const Bill = props => {
	const classes = useStyles();
	const theme = useTheme();

	return (
		<Paper elevation={3} className={classes.paper}>
			<Grid container spacing={1}>
				<Grid item xs className={classes.header}>
					{props.id ?
						<Typography variant="h6">{props.id}</Typography> :
						<Skeleton variant="text" animation="wave" height={22} width="10%" style={{marginBottom: theme.spacing(4)}}/>}
				</Grid>
				<Grid item xs={12}>
					{props.title ?
						<Typography variant="subtitle1" className={classes.indent}>{props.title}</Typography> :
						<Skeleton variant="text" animation="wave" height={22} width="80%" style={{marginBottom: theme.spacing(4)}}/>}
				</Grid>
				<Grid item xs={12} className={classes.header}>
					<Divider variant="middle"/>
				</Grid>
				<Grid item xs={12}>
					{props.summary ?
						<Typography className={classes.indent}>{props.summary}</Typography> :
						<Skeleton variant="text" animation="wave" height={18}/>}
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
