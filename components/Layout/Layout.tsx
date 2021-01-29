import Grid from '@material-ui/core/Grid';
import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Header from '@components/Header/Header';

export type LayoutProps = {
	children: React.ReactNode;
};

const Layout = ({children}: LayoutProps) => {
	const classes = useStyles();

	return (
		<div className={classes.root}>
			<Header/>
			<main>{children}</main>
		</div>
	);
};

const useStyles = makeStyles(() => ({
	root: {
		flexGrow: 1
	}
}));

export default Layout;
