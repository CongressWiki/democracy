import React from 'react';
import {CssBaseline} from '@material-ui/core';
import {createMuiTheme, ThemeProvider} from '@material-ui/core/styles';
import useLocalStorage from '@libs/use-local-storage';

const defaultState = {
	theme: 'dark',
	toggleDarkMode: () => null
};

export const ThemeContext = React.createContext(defaultState);

export const ThemeWrapper = ({children}: { children: React.ReactNode }) => {
	const [theme, setTheme] = useLocalStorage('theme', defaultState.theme);
	const toggleDarkMode = () => {
		setTheme(theme === 'light' ? 'dark' : 'light');
	};

	const nextTheme = React.useMemo(() => {
		const newTheme = createMuiTheme({
			palette: {
				type: theme,
				primary: {
					light: '#da452d',
					main: '#6c0000',
					dark: '#6c0000',
					contrastText: '#fff'
				},
				secondary: {
					light: '#ffffdd',
					main: '#edccab',
					dark: '#ba9b7c',
					contrastText: '#000'
				}
			},
			overrides: {
				// Style sheet name ⚛️
				MuiAppBar: {
					colorDefault: {
						backgroundColor: theme === 'dark' ? '#303030' : '#fff'
					}
				},
				MuiBackdrop: {
					root: {
						// BackgroundColor: '#fff'
					}
				}
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
				{children}
			</ThemeProvider>
		</ThemeContext.Provider>
	);
};
