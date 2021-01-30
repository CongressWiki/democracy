import React, {useContext} from 'react';
import {Tooltip, Badge, IconButton} from '@material-ui/core';
import {Brightness4 as Brightness4Icon} from '@material-ui/icons';
import {ThemeContext} from '@top-layer-layout/theme-wrapper';

const DarkModeToggle = () => {
	const {toggleDarkMode} = useContext(ThemeContext);
	return (
		<Tooltip title="Toggle dark mode">
			<IconButton color="inherit" onClick={toggleDarkMode}>
				<Badge color="secondary">
					<Brightness4Icon/>
				</Badge>
			</IconButton>
		</Tooltip>
	);
};

export default DarkModeToggle;
