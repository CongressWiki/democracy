import Header from './header';
import PropTypes from 'prop-types';
import React from 'react';
import {ThemeWrapper} from './theme-wrapper';

const TopLayout = props => {
	return (
		<>
			<Header/>
			<ThemeWrapper>
				{props.children}
			</ThemeWrapper>
		</>
	);
};

TopLayout.propTypes = {
	children: PropTypes.node
};

export default TopLayout;
