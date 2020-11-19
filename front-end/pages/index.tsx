import BillCanvas from '../components/bill-canvas';
import Layout from '../components/layout';
import React from 'react';
import {withApollo} from '../lib/with-apollo';

const Home = () => {
	return (
		<Layout>
			<BillCanvas/>
		</Layout>
	);
};

export default withApollo()(Home);
