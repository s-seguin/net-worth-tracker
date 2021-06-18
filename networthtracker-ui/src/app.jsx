import { makeStyles } from "@material-ui/core";
import React, { useState } from "react";

import { ContentContainer } from "./components/content-container";
import { Navbar } from "./components/navbar";
import { Sidebar } from "./components/sidebar";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
  },
}));

const pages = {
  overview: "Overview",
  assets: "Assets",
  liabilities: "Liabilities",
};

export const App = () => {
  const classes = useStyles();

  const [currentPage, setCurrentPage] = useState(pages.overview);

  return (
    <div className={classes.root}>
      <Navbar title={1} />
      <Sidebar pages={pages} setCurrentPage={setCurrentPage} />
      <ContentContainer>
        <p>{currentPage}</p>
      </ContentContainer>
    </div>
  );
};
