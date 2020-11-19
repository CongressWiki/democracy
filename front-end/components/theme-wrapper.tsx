import {ThemeProvider, createMuiTheme} from '@material-ui/core/styles';

import CssBaseline from '@material-ui/core/CssBaseline';
import PropTypes from 'prop-types';
import React from 'react';
import useLocalStorage from '../lib/use-local-storage';

const defaultState = {
	theme: 'light',
	toggleDarkMode: () => null
};

export const ThemeContext = React.createContext(defaultState);

export const ThemeWrapper = props => {
	const [theme, setTheme] = useLocalStorage('theme', 'light');
	const toggleDarkMode = () => {
		setTheme(theme === 'light' ? 'dark' : 'light');
	};

	const nextTheme = React.useMemo(() => {
		const newTheme = createMuiTheme({
			palette: {
				type: theme
			}
		});

		return newTheme;
	}, [theme]);

	return (
		<ThemeContext.Provider
			value={{
				theme,
				toggleDarkMode
			}}
		>
			<ThemeProvider theme={nextTheme}>
				<CssBaseline/>
				{props.children}
			</ThemeProvider>
		</ThemeContext.Provider>
	);
};

ThemeWrapper.propTypes = {
	children: PropTypes.node
};
