"use client";

import { createContext, useContext, useReducer, ReactNode } from "react";

interface AppState {
  title: string;
}

type AppAction =
  | { type: "SET_TITLE"; payload: string }
  | { type: "RESET_TITLE" };

interface AppContextType {
  state: AppState;
  setTitle: (title: string) => void;
  resetTitle: () => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

const initialState: AppState = {
  title: "Python by Example",
};

function appReducer(state: AppState, action: AppAction): AppState {
  switch (action.type) {
    case "SET_TITLE":
      return { ...state, title: action.payload };
    case "RESET_TITLE":
      return { ...state, title: "Python by Example" };
    default:
      return state;
  }
}

export function AppProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  const setTitle = (title: string) => {
    dispatch({ type: "SET_TITLE", payload: title });
  };

  const resetTitle = () => {
    dispatch({ type: "RESET_TITLE" });
  };

  return (
    <AppContext.Provider value={{ state, setTitle, resetTitle }}>
      {children}
    </AppContext.Provider>
  );
}

export function useAppState() {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error("useAppState must be used within an AppProvider");
  }
  return context;
}
