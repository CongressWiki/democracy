import React, {useContext} from 'react';
import {
	AppBar as MaterialUiAppBar,
	Toolbar,
	IconButton,
	Typography,
	MenuItem,
	Menu,
	useScrollTrigger,
	Theme
} from '@material-ui/core';
import {makeStyles, createStyles} from '@material-ui/core/styles';
import {MoreVert as MoreIcon} from '@material-ui/icons';
import DarkModeToggle from '@components/DarkModeToggle/DarkModeToggle';
import {ThemeContext} from '@top-layer-layout/theme-wrapper';

const AppBar = props => {
	const classes = useStyles();
	const [anchorElement, setAnchorElement] = React.useState<null | HTMLElement>(null);
	const [mobileMoreAnchorElement, setMobileMoreAnchorElement] = React.useState<null | HTMLElement>(null);

	const isMenuOpen = Boolean(anchorElement);
	const isMobileMenuOpen = Boolean(mobileMoreAnchorElement);

	const handleMobileMenuClose = () => {
		setMobileMoreAnchorElement(null);
	};

	const handleMenuClose = () => {
		setAnchorElement(null);
		handleMobileMenuClose();
	};

	const handleMobileMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
		setMobileMoreAnchorElement(event.currentTarget);
	};

	const menuId = 'primary-search-account-menu';
	const renderMenu = (
		<Menu
			keepMounted
			anchorEl={anchorElement}
			anchorOrigin={{vertical: 'top', horizontal: 'right'}}
			id={menuId}
			transformOrigin={{vertical: 'top', horizontal: 'right'}}
			open={isMenuOpen}
			onClose={handleMenuClose}
		>
			<DarkModeToggle/>
		</Menu>
	);

	const mobileMenuId = 'primary-search-account-menu-mobile';
	const {toggleDarkMode} = useContext(ThemeContext);
	const renderMobileMenu = (
		<Menu
			keepMounted
			anchorEl={mobileMoreAnchorElement}
			anchorOrigin={{vertical: 'top', horizontal: 'right'}}
			id={mobileMenuId}
			transformOrigin={{vertical: 'top', horizontal: 'right'}}
			open={isMobileMenuOpen}
			onClose={handleMobileMenuClose}
		>
			<MenuItem onClick={toggleDarkMode}>
				<DarkModeToggle/>
				<p>Toggle Dark Mode</p>
			</MenuItem>
		</Menu>
	);

	return (
		<div className={classes.grow}>
			<ElevationScroll {...props}>
				<MaterialUiAppBar color="default" position="fixed">
					<Toolbar variant="dense">
						<Typography noWrap className={classes.title} variant="h6">
							USA Counts
						</Typography>
						<div className={classes.grow}/>
						<div className={classes.sectionDesktop}>
							<DarkModeToggle/>
						</div>
						<div className={classes.sectionMobile}>
							<IconButton
								aria-label="show more"
								aria-controls={mobileMenuId}
								aria-haspopup="true"
								color="inherit"
								onClick={handleMobileMenuOpen}
							>
								<MoreIcon/>
							</IconButton>
						</div>
					</Toolbar>
				</MaterialUiAppBar>
			</ElevationScroll>
			<Toolbar className={classes.toolBar}/>
			{renderMobileMenu}
			{renderMenu}
		</div>
	);
};

function ElevationScroll({children}) {
	const trigger = useScrollTrigger({
		disableHysteresis: true,
		threshold: 0
	});

	return React.cloneElement(children, {
		elevation: trigger ? 4 : 0
	});
}

const useStyles = makeStyles((theme: Theme) =>
	createStyles({
		grow: {
			flexGrow: 1
		},
		menuButton: {
			marginRight: theme.spacing(4)
		},
		title: {
			display: 'none',
			[theme.breakpoints.up('sm')]: {
				display: 'block'
			}
		},
		sectionDesktop: {
			display: 'none',
			[theme.breakpoints.up('md')]: {
				display: 'flex'
			}
		},
		sectionMobile: {
			display: 'flex',
			[theme.breakpoints.up('md')]: {
				display: 'none'
			}
		},
		toolBar: {
			// MarginBottom: theme.spacing(2)
		}
	})
);
export default AppBar;
