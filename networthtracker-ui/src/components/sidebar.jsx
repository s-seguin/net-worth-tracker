import {
  Drawer,
  List,
  ListItem,
  ListItemText,
  makeStyles,
  Toolbar,
} from "@material-ui/core";
import PropTypes from "prop-types";
import React from "react";

const drawerWidth = 240;

const useStyles = makeStyles(() => ({
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  drawerContainer: {
    overflow: "auto",
  },
}));

export const Sidebar = ({ pages, setCurrentPage }) => {
  const classes = useStyles();

  return (
    <Drawer
      open={true}
      className={classes.drawer}
      variant="permanent"
      classes={{
        paper: classes.drawerPaper,
      }}
    >
      <Toolbar />
      <div className={classes.drawerContainer}>
        <List>
          {Object.values(pages).map((page) => (
            <ListItem button onClick={() => setCurrentPage(page)} key={page}>
              <ListItemText primary={page} />
            </ListItem>
          ))}
        </List>
      </div>
    </Drawer>
  );
};

Sidebar.propTypes = {
  pages: PropTypes.object,
  setCurrentPage: PropTypes.func,
};
