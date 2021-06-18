import { Container, makeStyles, Toolbar } from "@material-ui/core";
import React from "react";

const useStyles = makeStyles((theme) => ({
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
}));
export const ContentContainer = ({ children }) => {
  const classes = useStyles();

  return (
    <Container className={classes.content}>
      <Toolbar />
      {children}
    </Container>
  );
};
