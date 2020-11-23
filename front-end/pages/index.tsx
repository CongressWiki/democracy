import BillCanvas from '../components/BillCanvas';
import Layout from '../components/Layout';
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
