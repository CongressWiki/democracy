import BillCanvas from '../components/bill-canvas';
import Head from 'next/head';
import React from 'react';
import {withApollo} from '../lib/with-apollo';

const Home = () => {
	return (
		<div>
			<Head>
				<title>Keeping US Accountable</title>
				<link rel="icon" href="/favicon.ico"/>
			</Head>
			<main>
				<h1>USA Counts</h1>
				<p>Do our elected officials vote for us?</p>
				<div>
					<BillCanvas/>
				</div>
			</main>
		</div>
	);
};

export default withApollo()(Home);
