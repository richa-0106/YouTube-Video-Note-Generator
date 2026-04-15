const { app, BrowserWindow } = require("electron");

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
    },
  });

  mainWindow.loadURL("http://localhost:3000");

  mainWindow.webContents.openDevTools(); // DEBUG ke liye
}

app.whenReady().then(() => {
  createWindow();
});