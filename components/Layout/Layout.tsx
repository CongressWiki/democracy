import React from 'react';
import {Container} from '@material-ui/core';
import AppBar from '@components/AppBar/AppBar';

export type LayoutProps = {
	children: React.ReactNode;
};

const Layout = ({children}: LayoutProps) => {
	return (
		<>
			<AppBar/>
			<Container maxWidth="sm">
				{children}
			</Container>
		</>
	);
};

export default Layout;
