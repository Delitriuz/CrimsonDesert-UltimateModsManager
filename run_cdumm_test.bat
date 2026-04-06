@echo off
setlocal EnableDelayedExpansion

set "ROOT=%~dp0"
set "LOG=%ROOT%run_cdumm_test.log"
set "PY_EXE="
set "VENV_PY=%ROOT%.venv\Scripts\python.exe"

pushd "%ROOT%"
set "PYTHONPATH=%ROOT%src;%PYTHONPATH%"

echo ==== CDUMM test launcher ==== > "%LOG%"
echo Started: %DATE% %TIME%>> "%LOG%"

where py >nul 2>nul
if exist "%VENV_PY%" (
  set "PY_EXE=%VENV_PY%"
  goto :python_ready
)

if errorlevel 1 (
  echo [ERROR] Python launcher ^(py^) not found.
  echo [ERROR] Python launcher ^(py^) not found.>> "%LOG%"
  goto :fail
)

call :pick_python_from_launcher

if not defined PY_EXE (
  echo [ERROR] No usable Python 3.10/3.11/3.12 found.
  echo [ERROR] No usable Python 3.10/3.11/3.12 found.>> "%LOG%"
  echo Install Python 3.10-3.12 ^(non-WindowsApps build^) and retry.
  goto :fail
)

:python_ready
echo Using: %PY_EXE%
echo Using: %PY_EXE%>> "%LOG%"

"%PY_EXE%" -c "import PySide6" >nul 2>nul
if errorlevel 1 (
  echo [INFO] Installing dependencies...
  echo [INFO] Installing dependencies...>> "%LOG%"
  "%PY_EXE%" -m pip install -e . >> "%LOG%" 2>&1
  if errorlevel 1 (
    echo [ERROR] Failed to install dependencies. Check log:
    echo %LOG%
    echo [ERROR] Failed to install dependencies.>> "%LOG%"
    goto :fail
  )
)

echo Launching CDUMM...
echo Launching CDUMM...>> "%LOG%"
"%PY_EXE%" -m cdumm.main >> "%LOG%" 2>&1
set "APP_EXIT=%ERRORLEVEL%"

if not "%APP_EXIT%"=="0" (
  echo [ERROR] CDUMM exited with code %APP_EXIT%.
  echo [ERROR] CDUMM exited with code %APP_EXIT%.>> "%LOG%"
  echo Check log: %LOG%
  goto :fail
)

echo CDUMM exited normally.
echo CDUMM exited normally.>> "%LOG%"
goto :done

:pick_python_from_launcher
for /f "tokens=1,* delims= " %%A in ('py -0p ^| findstr /R /C:"-V:3\.12" /C:"-V:3\.11" /C:"-V:3\.10"') do (
  set "CANDIDATE=%%B"
  call :trim_candidate
  if defined CANDIDATE (
    echo !CANDIDATE! | findstr /I /C:"WindowsApps" >nul
    if errorlevel 1 (
      if exist "!CANDIDATE!" (
        set "PY_EXE=!CANDIDATE!"
        goto :eof
      )
    )
  )
)
goto :eof

:trim_candidate
setlocal EnableDelayedExpansion
set "TMP=%CANDIDATE%"
:trim_loop
if not defined TMP goto :trim_done
if "!TMP:~0,1!"==" " (
  set "TMP=!TMP:~1!"
  goto :trim_loop
)
:trim_done
endlocal & set "CANDIDATE=%TMP%"
goto :eof

:fail
echo.
echo Launcher finished with errors.
echo Log file: %LOG%
goto :pause_exit

:done
echo.
echo Launcher finished.
echo Log file: %LOG%

:pause_exit
popd
pause
endlocal
exit /b 0
