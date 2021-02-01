import React from 'react';
import TopLayout from '@top-layer-layout/top-layout';
import type {AppProps} from 'next/app';

const App = ({Component, pageProps}: AppProps) => {
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

export default App;
