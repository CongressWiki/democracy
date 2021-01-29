import Grid from "@material-ui/core/Grid";
import { Tooltip } from "@material-ui/core";
import React, { useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { ThemeContext } from "@top-layer-layout/theme-wrapper";
import IconButton from "@material-ui/core/IconButton";
import Badge from "@material-ui/core/Badge";
import Brightness4Icon from "@material-ui/icons/Brightness4";

export type LayoutProps = {
  children: React.ReactNode;
};

const Layout = ({ children }: LayoutProps) => {
  const classes = useStyles();
  const { toggleDarkMode } = useContext(ThemeContext);

  return (
    <div className={classes.root}>
      <Grid container spacing={0} justify="center">
        <Grid item xs={12} className={classes.header}>
          <h1>USA Counts</h1>
          <p>Do our elected officials vote for us?</p>
          <Tooltip title="Toggle dark mode">
            <IconButton color="inherit" onClick={toggleDarkMode}>
              <Badge color="secondary">
                <Brightness4Icon />
              </Badge>
            </IconButton>
          </Tooltip>
        </Grid>
        <Grid item xs>
          <main>{children}</main>
        </Grid>
      </Grid>
    </div>
  );
};

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
  },
  header: {
    left: "50vw",
    textAlign: "center",
  },
}));

export default Layout;
