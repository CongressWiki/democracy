// @xo-ignore
// import 'fontsource-roboto';

import CssBaseline from '@material-ui/core/CssBaseline';
import Head from 'next/head';
import PropTypes from 'prop-types';
import React from 'react';
import Theme from '../components/theme';
import {ThemeProvider} from '@material-ui/core/styles';

const App = props => {
	const {Component, pageProps} = props;

	React.useEffect(() => {
		// Remove the server-side injected CSS.
		const jssStyles = document.querySelector('#jss-server-side');
		if (jssStyles) {
			jssStyles.remove();
		}
	}, []);

	return (
		<>
			<Head>
				<title>My page</title>
				<meta name="viewport" content="minimum-scale=1, initial-scale=1, width=device-width"/>
			</Head>
			<ThemeProvider theme={Theme}>
				{/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
				<CssBaseline/>
				<Component {...pageProps}/>
			</ThemeProvider>
		</>
	);
};

App.propTypes = {
	Component: PropTypes.elementType.isRequired,
	pageProps: PropTypes.object.isRequired
};

export default App;
