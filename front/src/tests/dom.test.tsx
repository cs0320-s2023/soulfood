import "@testing-library/jest-dom";
import { act, fireEvent, render, screen } from "@testing-library/react";
// import userEvent from "@testing-library/user-event";
import App from "../App";
import { ListItemButton } from "@mui/material";

let homeButton: HTMLElement;
let exploreButton: HTMLElement;
let searchButton: HTMLElement;
let profileButton: HTMLElement;
let createButton: HTMLElement;

/** testing document-object model */

describe("test interactive functionality with frontend app", () => {
  beforeEach(() => {
    render(<App />);
    homeButton = screen.getByRole("home");
    exploreButton = screen.getByRole("explore");
    searchButton = screen.getByRole("search");
    profileButton = screen.getByRole("profile");
    createButton = screen.getByRole("create");
  });

  test("explore button exists on home page", async () => {
    expect(homeButton).not.toBeNull();

    act(() => {
      fireEvent.click(homeButton);
    });

    let explore = screen.getByRole("exploreButton");

    expect(explore).not.toBeNull();
  });

  test("submit button exists on create page", async () => {
    expect(createButton).not.toBeNull();

    act(() => {
      fireEvent.click(createButton);
    });

    let submit = screen.getByRole("createPageSubmitButton");

    expect(submit).not.toBeNull();
  });

  test("searching for an existing user will create a grid of cards on the screen", async () => {
    expect(searchButton).not.toBeNull();

    act(() => {
      fireEvent.click(searchButton);
    });

    let searchField = screen.getByLabelText("Search");
    let selectQuery = screen.getByRole("selectQuery");
    // let userQuery = screen.getByRole("userQuery");
    let submitSearch = screen.getByRole("submitSearch");

    act(() => {
      fireEvent.change(searchField, { target: { value: "1" } });
      fireEvent.click(selectQuery);
      fireEvent.keyDown(selectQuery, { key: "ArrowDown" });
      fireEvent.keyDown(selectQuery, { key: "ArrowDown" });
      fireEvent.keyUp(selectQuery, { key: "ArrowDown" });
      fireEvent.keyDown(selectQuery, { key: "Enter" });
      fireEvent.keyUp(selectQuery, { key: "Enter" });
      fireEvent.click(submitSearch);
    });

    let grid = screen.getByRole("grid");

    expect(grid).not.toBeNull();
  });

  test("testing signin functionality", async () => {
    let logout = screen.getByRole("logout");
    expect(logout).not.toBeNull();

    act(() => {
      fireEvent.click(logout);
    });

    // let signin = screen.getByRole("signin");
    expect(homeButton).toBeInTheDocument();
  });

  //   test("", async () => {

  //     expect(searchButton).not.toBeNull();

  //     act(() => {
  //       userEvent.click(searchButton);
  //     })

  //     let searchBox = screen.getByRole("searchBox")
  //     let label = screen.getByRole("label")
  //     let enterSearch = screen.getByRole("enterSearch")

  //     act(() => {
  //       userEvent.type(searchBox, "1")
  //       userEvent.click(enterSearch);
  //     })

  //   });

  // test("mode", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);

  //   const results = screen.queryByText("Command: load_file ten-star.csv");
  //   expect(results).not.toBeInTheDocument();

  //   await userEvent.type(inputBox, "mode");
  //   await userEvent.click(submitButton);

  //   const newResults = screen.queryByText("Command: load_file ten-star.csv");
  //   expect(newResults).toBeInTheDocument();
  // });

  // test("load_file", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);
  //   const accessibleResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command load_file ten-star.csv"
  //   });
  //   const results = screen.getByText("Success: The file at the path ten-star.csv has been successfully loaded.");
  //   expect(accessibleResults).toBeInTheDocument();
  //   expect(results).toBeInTheDocument();
  // });

  // test("load_file invalid file", async () => {
  //   await userEvent.type(inputBox, "load_file invalid-file.csv");
  //   await userEvent.click(submitButton);
  //   const accessibleResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command load_file invalid-file.csv"
  //   });
  //   const results = screen.getByText("Error: File not found.");
  //   expect(accessibleResults).toBeInTheDocument();
  //   expect(results).toBeInTheDocument();
  // });

  // test("view", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);

  //   const accessibleLoadResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command load_file ten-star.csv"
  //   });
  //   expect(accessibleLoadResults).toBeInTheDocument();

  //   await userEvent.type(inputBox, "view");
  //   await userEvent.click(submitButton);

  //   const accessibleViewResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command view"
  //   });
  //   expect(accessibleViewResults).toBeInTheDocument();

  //   const results = screen.getByRole("table")
  //   expect(results).toBeInTheDocument();
  // });

  // test("search", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);

  //   await userEvent.type(inputBox, "search ProperName 0");
  //   await userEvent.click(submitButton);

  //   const accessibleSearchResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command search ProperName 0"
  //   });
  //   expect(accessibleSearchResults).toBeInTheDocument();

  //   const results = screen.getByRole("table").innerHTML
  //   expect(results).toBe(
  //     "<tbody><tr><td>0</td><td>Sol</td><td>0</td><td>0</td><td>0</td></tr></tbody>"
  //   );
  // });

  // test("search invalid index", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);

  //   await userEvent.type(inputBox, "search 100 10");
  //   await userEvent.click(submitButton);

  //   const accessibleSearchResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command search 100 10"
  //   });
  //   expect(accessibleSearchResults).toBeInTheDocument();

  //   const results = screen.queryByText("Error: Could not find a column with such index.");
  //   expect(results).toBeInTheDocument();
  // });

  // test("search invalid name", async () => {
  //   await userEvent.type(inputBox, "load_file ten-star.csv");
  //   await userEvent.click(submitButton);

  //   await userEvent.type(inputBox, "search NotRealName 10");
  //   await userEvent.click(submitButton);

  //   const accessibleSearchResults = screen.getByRole("commandresult", {
  //     name: "You are currently at the result of command search NotRealName 10"
  //   });
  //   expect(accessibleSearchResults).toBeInTheDocument();

  //   const results = screen.queryByText("Error: Could not find a column with such name.");
  //   expect(results).toBeInTheDocument();
  // });
});
