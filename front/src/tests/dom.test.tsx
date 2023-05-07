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

});
