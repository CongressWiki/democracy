import Head from 'next/head';
import React from 'react';

export const siteTitle = 'Keeping US A-ccountable';

const Header = () => {
	return (
		<Head>
			<title>{siteTitle}</title>
			<meta
				name="description"
				content={siteTitle}
			/>
			<meta
				property="og:image"
				content={`https://og-image.now.sh/${encodeURI(
					siteTitle
				)}.png?theme=light&md=0&fontSize=75px&images=https%3A%2F%2Fassets.zeit.co%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fnextjs-black-logo.svg`}
			/>
			<meta name="og:title" content={siteTitle}/>
			<meta name="twitter:card" content="summary_large_image"/>
			<link rel="icon" href="/favicon.ico"/>
			<link
				href="https://fonts.googleapis.com/css?family=Roboto:400,500,700&display=swap"
				rel="stylesheet"
			/>
		</Head>
	);
};

export default Header;
