/*
 * TemperatureControlSystem.cpp : Defines the entry point for the application.
 */
#include "framework.h"
#include "TemperatureControlSystem.h"

/*
 * Main function
 */
int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPWSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: Place code here.

    // Initialize global strings
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_TEMPERATURECONTROLSYSTEM, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Perform application initialization:
    if (!InitInstance (hInstance, nCmdShow))
    {
        return FALSE;
    }

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_TEMPERATURECONTROLSYSTEM));

    MSG msg;

    // Main message loop:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int) msg.wParam;
}


ATOM MyRegisterClass(HINSTANCE hInstance)
{
    WNDCLASSEXW wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = hInstance;
    wcex.hIcon          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_TEMPERATURECONTROLSYSTEM));
    wcex.hCursor        = LoadCursor(nullptr, IDC_ARROW);
    wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.lpszMenuName   = MAKEINTRESOURCEW(IDC_TEMPERATURECONTROLSYSTEM);
    wcex.lpszClassName  = szWindowClass;
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassExW(&wcex);
}

BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   hInst = hInstance; // Store instance handle in our global variable
   int width = GetSystemMetrics(SM_CXSCREEN);// Get size width
   int heigth = GetSystemMetrics(SM_CYSCREEN);// Get size height

   HWND hWnd = CreateWindowW(
	   szWindowClass, 
	   szTitle, 
	   WS_OVERLAPPEDWINDOW,
	   CW_USEDEFAULT, CW_USEDEFAULT, 
	   width, heigth,
	   nullptr, 
	   nullptr, 
	   hInstance, 
	   nullptr);

   connect = CreateWindowW(
	   L"BUTTON",  // Predefined class; Unicode assumed 
	   L"Connect",      // Button text 
	   WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
	   10, 10,         // x ^ y position 
	   100, 50,        // width ^ heigth
	   hWnd,     // Parent window
	   NULL,       // No menu.
	   (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
	   NULL);      // Pointer not needed.

   modeOne = CreateWindowW(
	   L"BUTTON",  // Predefined class; Unicode assumed 
	   L"Mode 1",      // Button text 
	   WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
	   200, 10,         // x ^ y position 
	   100, 50,        // width ^ heigth
	   hWnd,     // Parent window
	   NULL,       // No menu.
	   (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
	   NULL);      // Pointer not needed.

   modeTwo = CreateWindowW(
	   L"BUTTON",  // Predefined class; Unicode assumed 
	   L"Mode 2",      // Button text 
	   WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
	   350, 10,         // x ^ y position 
	   100, 50,        // width ^ heigth
	   hWnd,     // Parent window
	   NULL,       // No menu.
	   (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
	   NULL);      // Pointer not needed.
   
   buttonSP = CreateWindowW(
	   L"BUTTON",  // Predefined class; Unicode assumed 
	   L"Start/Pause",      // Button text 
	   WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
	   (width*7)/8, heigth/4,         // x ^ y position 
	   100, 50,        // width ^ heigth
	   hWnd,     // Parent window
	   NULL,       // No menu.
	   (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
	   NULL);      // Pointer not needed.

   buttonCancel = CreateWindowW(
	   L"BUTTON",  // Predefined class; Unicode assumed 
	   L"Cancel",      // Button text 
	   WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,  // Styles 
	   (width * 7) / 8, (heigth / 4) + 70,         // x ^ y position 
	   100, 50,        // width ^ heigth
	   hWnd,     // Parent window
	   NULL,       // No menu.
	   (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
	   NULL);      // Pointer not needed.

   if (!hWnd)
   {
	   MessageBox(NULL,
		   _T("Call to CreateWindow failed!"),
		   _T("Windows Desktop Guided Tour"),
		   NULL);

	   return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	PAINTSTRUCT ps;
	HDC hdc = BeginPaint(hWnd, &ps);
	TCHAR bConnect[] = _T("Hello, connect!");
	TCHAR bMode1[] = _T("Hello, Mode 1!");
	TCHAR bMode2[] = _T("Hello, Mode 2!");
	TCHAR bSP[] = _T("Hello, Start/Pause!");
	TCHAR bCancel[] = _T("Hello, Cancel!");

	switch (message)
    {
    case WM_COMMAND:
        {
            int wmId = LOWORD(wParam);
            // Parse the menu selections:
            switch (wmId)
            {
            case IDM_ABOUT:
				{
					DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
				}        
                break;
            case IDM_EXIT:
				{
					DestroyWindow(hWnd);
				}
				break;                
			case BN_CLICKED:
				{
					if (hWnd == connect)
					{
						std::cout << "Connect!" << std::endl;
					}
					else if (modeOne)
					{
						std::cout << "Mode one" << std::endl;
					}
					else if (hWnd == modeTwo)
					{
						std::cout << "Mode two" << std::endl;
					}
					else if (hWnd == buttonSP)
					{
						std::cout << "Start/Pause" << std::endl;
					}
					else if (hWnd == buttonCancel)
					{
						std::cout << "Connect!" << std::endl;
					}
				}
				break;
            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;
    case WM_PAINT:
        {
			// TODO: Add any drawing code that uses hdc here...
            EndPaint(hWnd, &ps);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}