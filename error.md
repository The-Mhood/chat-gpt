mhoodpc PLAYABLE_ADANNA_M1% git rev-parse --short HEAD

UE_ROOT="/Users/Shared/Epic Games/UE_5.8" \
bash ./build_phase1_diagnostic.sh
4cd49c3
================================================================
 Phase-1 Unreal build diagnostic — 2026-11-22T11:51:24Z
 Persistent log: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T115124Z.log
 (If the terminal closes, this log file remains — cat it any time.)
================================================================
[diag] PASS  Engine found: UE_ROOT=/Users/Shared/Epic Games/UE_5.8
[diag] PASS  RunUAT.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/RunUAT.sh
[diag] PASS  Build.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh
[diag] PASS  GenerateProjectFiles.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh
[diag] PASS  Project file present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject
[diag] PASS  Module TDD_GAME declared in .uproject
[diag] PASS  Data header present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDOmegaValleyData.h
[diag] Generating project files (UBT must see Source/TDD_GAME)...
[diag] Exact command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh  /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject

Setting up Unreal Engine project files...

Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log_GPF.txt

Generating XCode project files:
Discovering modules, targets and source code for project...
Adding projects for all targets...
Adding projects for all targets took 0.23s
Adding projects for all game projects took 0.00s
Adding projects for all modules took 0.21s
DiscoverCSharpPrograms took 0.06s
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Adding additional Xcode project info took 1.70s
Compiling Rules Assemblies 100%
Creating Build Targets
Exception while creating build target for DotNetPerforceLib: Program targets are not currently supported from this engine distribution.
Exception while creating build target for ChaosTestHarness: Program targets are not currently supported from this engine distribution.
Exception while creating build target for EventLoopUnitTests: Program targets are not currently supported from this engine distribution.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Creating Build Targets 100%
Generating data for project indexing...
Creating Build Targets took 0.59s
Generating data for project indexing... 100%
Generating data for project indexing took 0.25s
Writing project files...
Writing xcode workspace /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME (Mac).xcworkspace
Writing project files... 100%
Writing project files took 1.32s
Compiling Rules Assemblies

Generating QueryTargets data for editor...
Compiling Rules Assemblies 100%
Writing Query Target Info 100%
Generating QueryTargets data for editor took 0.01s

Result: Succeeded
Total execution time: 7.19 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 134.0kb
[diag] PASS  GenerateProjectFiles.sh exited 0
[diag] Building TDD_GAME (Development / Mac) via Build.sh (UnrealBuildTool)...
[diag] Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64
@@TDD_BUILD_OUTPUT_BEGIN@@
Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Running dotnet Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.dll TDD_GAME Mac Development -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject -WaitMutex -architecture=arm64
Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log.txt
Determining max actions to execute in parallel (10 physical cores, 10 logical cores)
  Executing up to 10 processes, one per physical core
UbaServer - Listening on 0.0.0.0:1345
Invalidating makefile for TDD_GAME (ispc deleted)
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: warning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.
Compiling with Mac SDK 27.2, minimum Target OS version 14.00
UHT compiled-in object format Default
Building TDD_GAME...
===== Toolchain Information =====
Using Clang compiler 21.1.6 (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++)
  Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
Using Clang archiver (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool)
  Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
===== End Toolchain Information =====
Using Unreal Build Accelerator local executor to run 21 action(s)
  CPU 10 physical cores, 10 logical cores
  Memory 16 GB physical, 15.05 GB/16 GB committed
  UBA Storage capacity 40 GB
[1/21] Compile [Apple] SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h
[2/21] Compile [Apple] TDDLocationRegistry.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cpp:2:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   55 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cpp:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
   16 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cpp:14:28: note: 'BeginPlay' declared here
   14 | void UTDDLocationRegistry::BeginPlay()
      |                            ^
2 errors generated.
[3/21] Compile [Apple] TDDOmegaValleyGameMode.cpp
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameMode.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found
    4 | #include "TDDAdannaProxyCharacter.h"
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
[4/21] Compile [Apple] TDDCalendarSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.cpp:2:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   19 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.cpp:15:5: error: no member named 'BeginPlay' in 'UTickableWorldSubsystem'; did you mean simply 'BeginPlay'?
   15 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.cpp:13:29: note: 'BeginPlay' declared here
   13 | void UTDDCalendarSubsystem::BeginPlay()
      |                             ^
2 errors generated.
[5/21] Compile [Apple] TDDMarketSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp:2:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   53 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
   14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp:12:27: note: 'BeginPlay' declared here
   12 | void UTDDMarketSubsystem::BeginPlay()
      |                           ^
2 errors generated.
[6/21] Compile [Apple] TDDMarketStall.cpp
[7/21] Compile [Apple] TDDForbiddenForestGameMode.cpp
[8/21] Compile [Apple] TDDForbiddenForestLevel.cpp
[9/21] Compile [Apple] TDDNamedNPC.cpp
[10/21] Compile [Apple] Module.TDD_GAME.gen.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/arm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:3:
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   19 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/arm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:6:
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   55 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/arm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:8:
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   53 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/arm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:14:
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   51 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/arm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:16:
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   46 |     virtual void BeginPlay() override;
      |                  ^
5 errors generated.
[11/21] Compile [Apple] TDDAdannaProxyCharacter.cpp
[12/21] Compile [Apple] TDDSettlementZone.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.cpp:8:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   46 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.cpp:9:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   19 |     virtual void BeginPlay() override;
      |                  ^
2 errors generated.
[13/21] Compile [Apple] TDDPopulationActor.cpp
[14/21] Compile [Apple] TDDWorldPopulationSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubsystem.cpp:2:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   46 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
   14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubsystem.cpp:12:36: note: 'BeginPlay' declared here
   12 | void UTDDWorldPopulationSubsystem::BeginPlay()
      |                                    ^
2 errors generated.
[15/21] Compile [Apple] TDDWeatherSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:2:
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
   51 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
   14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:12:28: note: 'BeginPlay' declared here
   12 | void UTDDWeatherSubsystem::BeginPlay()
      |                            ^
2 errors generated.
[16/21] Compile [Apple] TDD_GAME.cpp
[17/21] Compile [Apple] TDDOmegaValleyLevel.cpp
Total time in Unreal Build Accelerator local executor: 23.66 seconds

Result: Failed (OtherCompilationError)
Total execution time: 26.95 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 19.1kb
@@TDD_BUILD_OUTPUT_END@@
[diag] FAIL  Build.sh exited 6 — C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.

================================================================
 BUILD FAILURE — C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.
 (exact command + diagnostics; also persisted in /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T115124Z.log)
================================================================
Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64

---- classification ----
  C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.

---- UHT activity (did UHT run?) ----
  UHT-related lines in build output: 6 (UHT was invoked/mentioned by UBT)
11:UHT compiled-in object format Default
74:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:
79:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:
84:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:
89:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:
94:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:

---- first meaningful compiler error (preserved) ----
26:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions

---- underlying exception / error detail (full capture, not tail) ----
26:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
29:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cpp:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
38:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameMode.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found
44:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
47:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.cpp:15:5: error: no member named 'BeginPlay' in 'UTickableWorldSubsystem'; did you mean simply 'BeginPlay'?
57:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
60:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
75:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
80:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
85:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
90:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
95:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
102:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
106:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
113:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
116:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
126:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
129:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?

---- last 60 lines of build output ----
   14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:12:28: note: 'BeginPlay' declared here
   12 | void UTDDWeatherSubsystem::BeginPlay()
      |                            ^
2 errors generated.
[16/21] Compile [Apple] TDD_GAME.cpp
[17/21] Compile [Apple] TDDOmegaValleyLevel.cpp
Total time in Unreal Build Accelerator local executor: 23.66 seconds

Result: Failed (OtherCompilationError)
Total execution time: 26.95 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 19.1kb
@@TDD_BUILD_OUTPUT_END@@
[diag] FAIL  Build.sh exited 6 — C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.

================================================================
 BUILD FAILURE — C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.
 (exact command + diagnostics; also persisted in /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T115124Z.log)
================================================================
Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64

---- classification ----
  C++ COMPILATION FAILED — the Clang C++ compiler started and reported errors (UHT had already succeeded; UHT-generated .gen.cpp files appearing in the compiler output are normal include traces, NOT a UHT rejection). Fix C++ with Engineering.

---- UHT activity (did UHT run?) ----
  UHT-related lines in build output: 6 (UHT was invoked/mentioned by UBT)
11:UHT compiled-in object format Default
74:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:
79:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:
84:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:
89:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:
94:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/UnrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:

---- first meaningful compiler error (preserved) ----
26:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions

---- underlying exception / error detail (full capture, not tail) ----
26:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
29:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cpp:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
38:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameMode.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found
44:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
47:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.cpp:15:5: error: no member named 'BeginPlay' in 'UTickableWorldSubsystem'; did you mean simply 'BeginPlay'?
57:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
60:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
75:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
80:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions
85:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions
90:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
95:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
102:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
106:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions
113:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions
116:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?
126:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions
129:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?

---- last 60 lines of build output ----
                                                                                             
[diag] ACTION: send the full log (/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T115124Z.log) to Engineering. Do NOT fix C++ yourself.
[diag] Engineering owns all Phase-1 C++ fixes. Phase 1 remains IMPLEMENTED_UNVERIFIED.
mhoodpc PLAYABLE_ADANNA_M1% 