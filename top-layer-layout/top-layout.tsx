import React from 'react';
import Header from './header';
import {ThemeWrapper} from './theme-wrapper';

const TopLayout = ({children}: {children: React.ReactNode}) => {
	return (
		<>
			<Header/>
			<ThemeWrapper>
				{children}
			</ThemeWrapper>
		</>
	);
};

export default TopLayout;
