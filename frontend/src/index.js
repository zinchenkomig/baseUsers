import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import {AuthProvider} from "./context/auth";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query"
import {ReactQueryDevtools} from "@tanstack/react-query-devtools";



const queryClient = new QueryClient()

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
          <QueryClientProvider client={queryClient}>
              <AuthProvider>
                  <App />
              </AuthProvider>
              <ReactQueryDevtools/>
          </QueryClientProvider>
  </React.StrictMode>
);

