#pragma once

#include <windows.h>
#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <string.h>
#include <tchar.h>
#include <winusb.h>
#include "resource.h"

#define MAX_LOADSTRING 100

/*
 * Global Variables:
 */
HINSTANCE hInst;                                // Current instance
WCHAR szTitle[MAX_LOADSTRING];                  // The title bar text
WCHAR szWindowClass[MAX_LOADSTRING];            // The main window class name
HWND connect;									// Button connect
HWND modeOne;									// Button modeOne
HWND modeTwo;									// Button modeTwo
HWND buttonSP;									// Button Start/Pause
HWND buttonCancel;								// Button cancel

/*
 * Forward declarations of functions included in this code module:
 */
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);

/*
 * FUNCTION: MyRegisterClass()
 * PURPOSE: Registers the window class.
 */
ATOM MyRegisterClass(HINSTANCE hInstance);

/*
 * FUNCTION: InitInstance(HINSTANCE, int)
 * PURPOSE: Saves instance handle and creates main window
 * COMMENTS: In this function, we save the instance handle in a global variable and
 * create and display the main program window.
 */
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow);

/*
 * FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)
 * PURPOSE: Processes messages for the main window.
 * WM_COMMAND  - process the application menu
 * WM_PAINT    - Paint the main window
 * WM_DESTROY  - post a quit message and return
 */
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);

/*
 * Message handler for about box.
 */
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam);

/*
 * PURPOSE: Recognize USB device
 * DeviceHandle - O identificador para o dispositivo que CreateFile retornou.
 * InterfaceHandle - Receives an opaque handle to the first (default)
 * interface on the device. 
 */