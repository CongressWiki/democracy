import {Theme, createStyles, makeStyles} from '@material-ui/core/styles';

import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import React from 'react';

const useStyles = makeStyles((theme: Theme) => (
	createStyles({
		root: {
			flexGrow: 1,
			justifyContent: 'center'
		},
		paper: {
			padding: theme.spacing(2),
			textAlign: 'center',
			color: theme.palette.text.secondary
		}
	}))
);

const Layout = ({
	children
}: {
	children: React.ReactNode;
}) => {
	const classes = useStyles();

	return (
		<div className={classes.root}>
			<Grid container spacing={3}>
				<Grid item xs={12}>
					<h1>USA Counts</h1>
					<p>Do our elected officials vote for us?</p>
				</Grid>
				<Grid item xs={12}>
					<main>{children}</main>
				</Grid>
			</Grid>
		</div>
	);
};

export default Layout;
