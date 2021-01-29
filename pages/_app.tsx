import PropTypes from 'prop-types';
import React from 'react';
import TopLayout from '@top-layer-layout/top-layout';

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
		<TopLayout>
			<Component {...pageProps}/>
		</TopLayout>
	);
};

App.propTypes = {
	Component: PropTypes.elementType.isRequired,
	pageProps: PropTypes.object.isRequired
};

export default App;
