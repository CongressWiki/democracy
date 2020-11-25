import Header from './header';
import PropTypes from 'prop-types';
import React from 'react';
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

TopLayout.propTypes = {
	children: PropTypes.node
};

export default TopLayout;
