import Grid from "@material-ui/core/Grid";
import React from "react";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    // backgroundImage: 'url("https://www.transparenttextures.com/patterns/purty-wood.png")',
    // backgroundColor: "#edccab",
  },
  header: {
    left: "50vw",
    textAlign: "center",
    position: "fixed",
  },
}));

const Layout = ({ children }: { children: React.ReactNode }) => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12} className={classes.header}>
          <h1>USA Counts</h1>
          <p>Do our elected officials vote for us?</p>
        </Grid>
        <Grid item xs={4}>
          <main>{children}</main>
        </Grid>
      </Grid>
    </div>
  );
};

export default Layout;
