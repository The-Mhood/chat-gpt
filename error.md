zsh: command not found: #
note     descriptor TDD_GAME.uproject parses
note     TDD_GAME.Target.cs: build settings BuildSettingsVersion.V7, include order EngineIncludeOrderVersion.Unreal5_
8, modules ['TDD_GAME']                                                                                              note     TDD_GAMEEditor.Target.cs: build settings BuildSettingsVersion.V7, include order EngineIncludeOrderVersion.Un
real5_8, modules ['TDD_GAME']                                                                                        
  0 blocker(s), 0 warning(s). Static check only: nothing was built.
zsh: command not found: #
PASS [gpf_fail] rc=3 label='PROJECT FILE GENERATION FAILED'
PASS [uht] rc=1 label='UHT / HEADER PARSE FAILED'
PASS [compile] rc=1 label='C++ COMPILATION FAILED'
PASS [link] rc=1 label='LINKING FAILED'
PASS [invocation] rc=1 label='BUILD INVOCATION FAILED'
PASS [aggregate_uht] rc=1 label='UHT / HEADER PARSE FAILED'
PASS [aggregate_unknown] rc=1 label='UBT EXCEPTION'
PASS [uht_token_only] rc=1 label='unclassified'
PASS [ok] rc=0 label='SUCCESS'

classifier regression: 9 PASS / 0 FAIL
zsh: command not found: #
================================================================
 Phase-1 Unreal build diagnostic — 2026-11-22T11:36:35Z
 Persistent log: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_20261122T113635Z.log
 (If the terminal closes, this log file remains — cat it any time.)
================================================================
[diag] PASS  Engine found: UE_ROOT=/Users/Shared/Epic Games/UE_5.8
[diag] PASS  RunUAT.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/RunUAT.sh
[diag] PASS  Build.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh
[diag] PASS  GenerateProjectFiles.sh located: /Users/Shared/Epic Games/UE_5.8/Engine/Build/BatchFiles/Mac/GeneratePro
jectFiles.sh                                                                                                         [diag] PASS  Project file present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.up
roject                                                                                                               [diag] PASS  Module TDD_GAME declared in .uproject
[diag] PASS  Data header present: /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_G
AME/Public/TDDOmegaValleyData.h                                                                                      [diag] Generating project files (UBT must see Source/TDD_GAME)...
[diag] Exact command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/GenerateProjectFiles.sh  /Users/mhoodpc/TDD/TDD_PHASE3
_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject                                                          
Setting up Unreal Engine project files...

Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log_GPF.txt

Generating XCode project files:
Discovering modules, targets and source code for project...
Adding projects for all targets...
Adding projects for all targets took 0.22s
Adding projects for all game projects took 0.00s
Adding projects for all modules took 0.21s
DiscoverCSharpPrograms took 0.05s
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: wa
rning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.                                                                           /Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: wa
rning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.                                                                           Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Adding additional Xcode project info took 1.78s
Compiling Rules Assemblies 100%
Creating Build Targets
Exception while creating build target for ChaosTestHarness: Program targets are not currently supported from this eng
ine distribution.                                                                                                    Exception while creating build target for EventLoopUnitTests: Program targets are not currently supported from this e
ngine distribution.                                                                                                  Exception while creating build target for DotNetPerforceLib: Program targets are not currently supported from this en
gine distribution.                                                                                                   /Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: wa
rning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.                                                                           /Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: wa
rning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.                                                                           Creating Build Targets 100%
Generating data for project indexing...
Creating Build Targets took 0.57s
Generating data for project indexing... 100%
Generating data for project indexing took 0.28s
Writing project files...
Writing xcode workspace /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME (Mac).xcworks
pace                                                                                                                 Writing project files... 100%
Writing project files took 1.24s

Generating QueryTargets data for editor...
Compiling Rules Assemblies 100%
Writing Query Target Info 100%
Generating QueryTargets data for editor took 0.01s

Result: Succeeded
Total execution time: 7.06 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 134.0kb
[diag] PASS  GenerateProjectFiles.sh exited 0
[diag] Building TDD_GAME (Development / Mac) via Build.sh (UnrealBuildTool)...
[diag] Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/
mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64   @@TDD_BUILD_OUTPUT_BEGIN@@
Setting up bundled DotNet SDK
/Users/Shared/Epic Games/UE_5.8/Engine/Binaries/ThirdParty/DotNet/10.0/mac-arm64
Running dotnet Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.dll TDD_GAME Mac Development -project=/Users/mh
oodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject -WaitMutex -architecture=arm64       Log file: /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Log.txt
Determining max actions to execute in parallel (10 physical cores, 10 logical cores)
  Executing up to 10 processes, one per physical core
UbaServer - Listening on 0.0.0.0:1345
Invalidating makefile for TDD_GAME (ispc deleted)
/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/MetalShaderConverter.build.cs: wa
rning: Referenced directory '/Users/Shared/Epic Games/UE_5.8/Engine/Source/ThirdParty/Apple/MetalShaderConverter/include/metal_irconverter_ext' does not exist.                                                                           Compiling with Mac SDK 27.2, minimum Target OS version 14.00
Building TDD_GAME...
===== Toolchain Information =====
Using Clang compiler 21.1.6 (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c
lang++)                                                                                                                Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /A
pplications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin                                 Using Clang archiver (/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool)
  Apple clang version 21.0.0 (clang-2100.4.1.1) Target: arm64-apple-darwin27.2.0 Thread model: posix InstalledDir: /A
pplications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin                                 ===== End Toolchain Information =====
Using Unreal Build Accelerator local executor to run 21 action(s)
  CPU 10 physical cores, 10 logical cores
  Memory 16 GB physical, 14.5 GB/16 GB committed
  UBA Storage capacity 40 GB
[1/21] Compile [Apple] SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h
[2/21] Compile [Apple] TDDOmegaValleyGameMode.cpp
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameMode
.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found                                                       4 | #include "TDDAdannaProxyCharacter.h"
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
[3/21] Compile [Apple] TDDMarketStall.cpp
[4/21] Compile [Apple] TDDMarketSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDMarketSubsystem.cpp:2:                                                                                            /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53
:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                    53 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp
:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                        14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp
:12:27: note: 'BeginPlay' declared here                                                                                 12 | void UTDDMarketSubsystem::BeginPlay()
      |                           ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.cpp
:50:36: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?        50 |             Out.Stalls = S.Kind == TDDWorld::ESettlementKind::Town ? 24 : 14;
      |                                    ^~~~~~~~~~~~~~~~~~~~~~~~~
      |                                    ESettlementKind
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldLogic.h:55:12: 
note: 'ESettlementKind' declared here                                                                                   55 | enum class ESettlementKind : uint8
      |            ^
3 errors generated.
[5/21] Compile [Apple] TDDCalendarSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDCalendarSubsystem.cpp:2:                                                                                          /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                  19 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
20:18: error: 'Tick' marked 'override' but does not override any member functions                                       20 |     virtual void Tick(float DeltaSeconds) override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                      14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:12:29: note: 'BeginPlay' declared here                                                                               12 | void UTDDCalendarSubsystem::BeginPlay()
      |                             ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDCalendarSubsystem.cpp:1:                                                                                          In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/TDD_GAME/Development/Engine/SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h:4:                                In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Slate/Public/SlateSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/CoreUObject/Public/CoreUObjectSharedPCH.h
:5:                                                                                                                  In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/CoreSharedPCH.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Algo/Reverse.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Templates/UnrealTemplate.h:7:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/UnrealMemory.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/GenericPlatform/GenericPlatfo
rmMemory.h:12:                                                                                                       In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/PlatformString.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Mac/MacPlatformString.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Apple/ApplePlatformString.h:7
:                                                                                                                    In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Misc/AssertionMacros.h:10:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:61:
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: stati
c assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.      15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:54: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:17:5: note: in instantiation of function template specialization 'UE::Core::Private::FormatStringSan::AssertFormatStatus<UE::Core::Private::FormatStringSan::EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow, UE::Core::Private::FormatStringSan::TAtArgPos<1>>' requested here                                                                       17 |     UE_LOG(LogTemp, Display,
      |     ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:281:3: note: expanded from macr
o 'UE_LOG'                                                                                                             281 |         UE_PRIVATE_LOG(UE_EMPTY, constexpr, CategoryName, Verbosity, Format, ##__VA_ARGS__) \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:339:3: note: expanded from macr
o 'UE_PRIVATE_LOG'                                                                                                     339 |         UE_VALIDATE_FORMAT_STRING(Format, ##__VA_ARGS__); \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:27:36: note: expanded from
 macro 'UE_VALIDATE_FORMAT_STRING'                                                                                      27 |     #define UE_VALIDATE_FORMAT_STRING UE_CHECK_FORMAT_STRING
      |                                       ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:19:10: note: expanded from
 macro 'UE_CHECK_FORMAT_STRING'                                                                                         19 |         (UCFS::AssertFormatStatus<UCFS_Result.Status, UCFS::TAtArgPos<UCFS_Result.ArgPos>>()); \
      |                ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: note: expres
sion evaluates to '7 != 7'                                                                                              15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:58: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:24:12: error: no type named 'Tick' in 'UWorldSubsystem'                                                              24 |     Super::Tick(DeltaSeconds);
      |     ~~~~~~~^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:24:17: error: declaration shadows a local variable [-Werror,-Wshadow]                                                24 |     Super::Tick(DeltaSeconds);
      |                 ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:22:40: note: previous declaration is here                                                                            22 | void UTDDCalendarSubsystem::Tick(float DeltaSeconds)
      |                                        ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDCalendarSubsystem.cpp:1:                                                                                          In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/TDD_GAME/Development/Engine/SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h:4:                                In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Slate/Public/SlateSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/CoreUObject/Public/CoreUObjectSharedPCH.h
:5:                                                                                                                  In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/CoreSharedPCH.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Algo/Reverse.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Templates/UnrealTemplate.h:7:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/UnrealMemory.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/GenericPlatform/GenericPlatfo
rmMemory.h:12:                                                                                                       In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/PlatformString.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Mac/MacPlatformString.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Apple/ApplePlatformString.h:7
:                                                                                                                    In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Misc/AssertionMacros.h:10:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:61:
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: stati
c assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.      15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:54: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsystem.c
pp:36:5: note: in instantiation of function template specialization 'UE::Core::Private::FormatStringSan::AssertFormatStatus<UE::Core::Private::FormatStringSan::EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow, UE::Core::Private::FormatStringSan::TAtArgPos<2>>' requested here                                                                       36 |     UE_LOG(LogTemp, Display,
      |     ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:281:3: note: expanded from macr
o 'UE_LOG'                                                                                                             281 |         UE_PRIVATE_LOG(UE_EMPTY, constexpr, CategoryName, Verbosity, Format, ##__VA_ARGS__) \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:339:3: note: expanded from macr
o 'UE_PRIVATE_LOG'                                                                                                     339 |         UE_VALIDATE_FORMAT_STRING(Format, ##__VA_ARGS__); \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:27:36: note: expanded from
 macro 'UE_VALIDATE_FORMAT_STRING'                                                                                      27 |     #define UE_VALIDATE_FORMAT_STRING UE_CHECK_FORMAT_STRING
      |                                       ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:19:10: note: expanded from
 macro 'UE_CHECK_FORMAT_STRING'                                                                                         19 |         (UCFS::AssertFormatStatus<UCFS_Result.Status, UCFS::TAtArgPos<UCFS_Result.ArgPos>>()); \
      |                ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: note: expres
sion evaluates to '7 != 7'                                                                                              15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:58: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
7 errors generated.
[6/21] Compile [Apple] TDDLocationRegistry.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDLocationRegistry.cpp:2:                                                                                           /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:5
5:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                   55 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                       16 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:14:28: note: 'BeginPlay' declared here                                                                                14 | void UTDDLocationRegistry::BeginPlay()
      |                            ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:25:18: error: indirection requires pointer operand ('FName' invalid)                                                  25 |         Rec.Id = *FName(S.Id.c_str());
      |                  ^~~~~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:27:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?       27 |         Rec.Access = (S.Kind == TDDWorld::ESettlementKind::Town ||
      |                                 ^~~~~~~~~~~~~~~~~~~~~~~~~
      |                                 ESettlementKind
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldLogic.h:55:12: 
note: 'ESettlementKind' declared here                                                                                   55 | enum class ESettlementKind : uint8
      |            ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:28:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?       28 |                       S.Kind == TDDWorld::ESettlementKind::MarketTown)
      |                                 ^~~~~~~~~~~~~~~~~~~~~~~~~
      |                                 ESettlementKind
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldLogic.h:55:12: 
note: 'ESettlementKind' declared here                                                                                   55 | enum class ESettlementKind : uint8
      |            ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistry.cp
p:77:13: error: invalid argument type 'FSetElementId' to unary expression                                               77 |         if (!Seen.Add(Rec.Id))
      |             ^~~~~~~~~~~~~~~~~
6 errors generated.
[7/21] Compile [Apple] TDDForbiddenForestLevel.cpp
[8/21] Compile [Apple] TDDNamedNPC.cpp
[9/21] Compile [Apple] TDDForbiddenForestGameMode.cpp
[10/21] Compile [Apple] Module.TDD_GAME.gen.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:3:                                                      In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/U
nrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:                                                           /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                  19 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
20:18: error: 'Tick' marked 'override' but does not override any member functions                                       20 |     virtual void Tick(float DeltaSeconds) override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:6:                                                      In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/U
nrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:                                                            /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry.h:5
5:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                   55 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:8:                                                      In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/U
nrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:                                                             /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h:53
:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                    53 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:14:                                                     In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/U
nrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:                                                            /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:5
1:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                   51 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/UnrealGame/Development/TDD_GAME/Module.TDD_GAME.gen.cpp:16:                                                     In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/U
nrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:                                                    /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsy
stem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           46 |     virtual void BeginPlay() override;
      |                  ^
6 errors generated.
[11/21] Compile [Apple] TDDAdannaProxyCharacter.cpp
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/TDDAdannaProxyCharacter.cpp:19
8:50: error: no matching constructor for initialization of 'TActorIterator<ATDDForbiddenForestLevel>'                  198 |     if (TActorIterator<ATDDForbiddenForestLevel> It(GetWorld(), EActorIteratorFlags::AllActors); It)
      |                                                  ^  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineUtils.h:582:11: note: candidate constructor
 not viable: no known conversion from 'EActorIteratorFlags' to 'TSubclassOf<ATDDForbiddenForestLevel>' for 2nd argument                                                                                                                     582 |     explicit TActorIterator(const UWorld* InWorld, TSubclassOf<ActorType> InClass = ActorType::StaticClass(),
 EActorIteratorFlags InFlags = EActorIteratorFlags::OnlyActiveLevels | EActorIteratorFlags::SkipPendingKill)               |              ^                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineUtils.h:591:11: note: candidate constructor
 not viable: requires 1 argument, but 2 were provided                                                                  591 |     explicit TActorIterator(EActorIteratorType)
      |              ^              ~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineUtils.h:569:7: note: candidate constructor 
(the implicit copy constructor) not viable: requires 1 argument, but 2 were provided                                   569 | class TActorIterator : public TActorIteratorBase<TActorIterator<ActorType>>
      |       ^~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineUtils.h:569:7: note: candidate constructor 
(the implicit move constructor) not viable: requires 1 argument, but 2 were provided                                   569 | class TActorIterator : public TActorIteratorBase<TActorIterator<ActorType>>
      |       ^~~~~~~~~~~~~~
1 error generated.
[12/21] Compile [Apple] TDDOmegaValleyLevel.cpp
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:126:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                          126 |     UInstancedStaticMeshComponent* ValleyForestFloor = CreateInstancePool(TEXT("FOREST_FLOOR"), ValleyCubeMes
h, true, ValleyForestFloor);                                                                                               |                                    ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:25:24: note: previous declaration is here                                                                             25 |     const FLinearColor ValleyForestFloor(0.12f, 0.18f, 0.12f, 1.0f);
      |                        ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:126:119: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                              126 |     UInstancedStaticMeshComponent* ValleyForestFloor = CreateInstancePool(TEXT("FOREST_FLOOR"), ValleyCubeMes
h, true, ValleyForestFloor);                                                                                               |                                                                                                              
         ^~~~~~~~~~~~~~~~~                                                                                           /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:38:82: note: passing argument to parameter 'Tint' here                                                                38 |     const FName& Name, const TCHAR* MeshPath, bool bCollide, const FLinearColor& Tint)
      |                                                                                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:127:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                          127 |     UInstancedStaticMeshComponent* ValleyCanopy = CreateInstancePool(TEXT("FOREST_CANOPY"), ValleyCylinderMes
h, false, ValleyCanopy);                                                                                                   |                                    ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:26:24: note: previous declaration is here                                                                             26 |     const FLinearColor ValleyCanopy(0.10f, 0.24f, 0.15f, 1.0f);
      |                        ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:127:120: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                              127 |     UInstancedStaticMeshComponent* ValleyCanopy = CreateInstancePool(TEXT("FOREST_CANOPY"), ValleyCylinderMes
h, false, ValleyCanopy);                                                                                                   |                                                                                                              
          ^~~~~~~~~~~~                                                                                               /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLevel.cp
p:38:82: note: passing argument to parameter 'Tint' here                                                                38 |     const FName& Name, const TCHAR* MeshPath, bool bCollide, const FLinearColor& Tint)
      |                                                                                  ^
4 errors generated.
[13/21] Compile [Apple] TDDSettlementZone.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDSettlementZone.cpp:8:                                                                                             /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsy
stem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           46 |     virtual void BeginPlay() override;
      |                  ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDSettlementZone.cpp:9:                                                                                             /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                  19 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem.h:
20:18: error: 'Tick' marked 'override' but does not override any member functions                                       20 |     virtual void Tick(float DeltaSeconds) override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.cpp:
83:26: error: no viable conversion from 'const FTDDActiveTierCounts' to 'const TDDWorld::FActiveTierCounts'             83 |     SpawnPopulationTiers(Counts);
      |                          ^~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldLogic.h:340:8: 
note: candidate constructor (the implicit copy constructor) not viable: no known conversion from 'const FTDDActiveTierCounts' to 'const FActiveTierCounts &' for 1st argument                                                               340 | struct FActiveTierCounts
      |        ^~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldLogic.h:340:8: 
note: candidate constructor (the implicit move constructor) not viable: no known conversion from 'const FTDDActiveTierCounts' to 'FActiveTierCounts &&' for 1st argument                                                                    340 | struct FActiveTierCounts
      |        ^~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDSettlementZone.h:54:
66: note: passing argument to parameter 'Counts' here                                                                   54 |     void SpawnPopulationTiers(const TDDWorld::FActiveTierCounts& Counts);
      |                                                                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.cpp:
118:53: error: no member named 'ToString' in 'FString'                                                                 118 |                 Actor->SetOccupation(SettlementName.ToString());
      |                                      ~~~~~~~~~~~~~~ ^
5 errors generated.
[14/21] Compile [Apple] TDDPopulationActor.cpp
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDPopulationActor.cpp
:51:30: error: no member named 'GetRandInteger' in 'FMath'                                                              51 |     FRandomStream Rng(FMath::GetRandInteger(0, INT32_MAX));
      |                              ^~~~~~~~~~~~~~
1 error generated.
[15/21] Compile [Apple] TDDWeatherSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDWeatherSubsystem.cpp:2:                                                                                           /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem.h:5
1:18: error: 'BeginPlay' marked 'override' but does not override any member functions                                   51 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cp
p:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                       14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cp
p:12:28: note: 'BeginPlay' declared here                                                                                12 | void UTDDWeatherSubsystem::BeginPlay()
      |                            ^
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDWeatherSubsystem.cpp:1:                                                                                           In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/Mac/a
rm64/TDD_GAME/Development/Engine/SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.h:4:                                In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Engine/Public/EngineSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Slate/Public/SlateSharedPCH.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/CoreUObject/Public/CoreUObjectSharedPCH.h
:5:                                                                                                                  In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/CoreSharedPCH.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Algo/Reverse.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Templates/UnrealTemplate.h:7:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/UnrealMemory.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/GenericPlatform/GenericPlatfo
rmMemory.h:12:                                                                                                       In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/HAL/PlatformString.h:6:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Mac/MacPlatformString.h:5:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Apple/ApplePlatformString.h:7
:                                                                                                                    In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Misc/AssertionMacros.h:10:
In file included from /Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:61:
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: stati
c assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.      15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:54: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsystem.cp
p:16:5: note: in instantiation of function template specialization 'UE::Core::Private::FormatStringSan::AssertFormatStatus<UE::Core::Private::FormatStringSan::EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow, UE::Core::Private::FormatStringSan::TAtArgPos<0>>' requested here                                                                        16 |     UE_LOG(LogTemp, Display,
      |     ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:281:3: note: expanded from macr
o 'UE_LOG'                                                                                                             281 |         UE_PRIVATE_LOG(UE_EMPTY, constexpr, CategoryName, Verbosity, Format, ##__VA_ARGS__) \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/Logging/LogMacros.h:339:3: note: expanded from macr
o 'UE_PRIVATE_LOG'                                                                                                     339 |         UE_VALIDATE_FORMAT_STRING(Format, ##__VA_ARGS__); \
      |         ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:27:36: note: expanded from
 macro 'UE_VALIDATE_FORMAT_STRING'                                                                                      27 |     #define UE_VALIDATE_FORMAT_STRING UE_CHECK_FORMAT_STRING
      |                                       ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:19:10: note: expanded from
 macro 'UE_CHECK_FORMAT_STRING'                                                                                         19 |         (UCFS::AssertFormatStatus<UCFS_Result.Status, UCFS::TAtArgPos<UCFS_Result.ArgPos>>()); \
      |                ^
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: note: expres
sion evaluates to '7 != 7'                                                                                              15 | X(SNeedsWideCharPtrArgButGotNarrow, "'%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.")
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSan.h:60:58: note: expanded from
 macro 'X'                                                                                                              60 |                 case EFormatStringSanStatus::Name: static_assert(Err != EFormatStringSanStatus::Name, Desc); 
break;                                                                                                                     |                                                                  ~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3 errors generated.
[16/21] Compile [Apple] TDDWorldPopulationSubsystem.cpp
In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/
TDDWorldPopulationSubsystem.cpp:2:                                                                                   /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationSubsy
stem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           46 |     virtual void BeginPlay() override;
      |                  ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubs
ystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?               14 |     Super::BeginPlay();
      |     ^~~~~~~~~~~~~~~~
      |     BeginPlay
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubs
ystem.cpp:12:36: note: 'BeginPlay' declared here                                                                        12 | void UTDDWorldPopulationSubsystem::BeginPlay()
      |                                    ^
/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulationSubs
ystem.cpp:36:40: error: no member named 'ValueOrDefault' in 'TMap<FName, int>'                                          36 |     return SettlementLogicalPopulation.ValueOrDefault(SettlementId, 0);
      |            ~~~~~~~~~~~~~~~~~~~~~~~~~~~ ^
3 errors generated.
[17/21] Compile [Apple] TDD_GAME.cpp
Total time in Unreal Build Accelerator local executor: 27.26 seconds

Result: Failed (OtherCompilationError)
Total execution time: 28.92 seconds
Trace written to file /Users/mhoodpc/Library/Application Support/Epic/UnrealBuildTool/Trace.uba with size 47.8kb
@@TDD_BUILD_OUTPUT_END@@
[diag] FAIL  Build.sh exited 6 — UHT / HEADER PARSE FAILED — Unreal Header Tool rejected the reflected declarations (
a reflection/metadata error, NOT a C++ compile error). Fix UENUM/USTRUCT/UCLASS annotations with Engineering.        
================================================================
 BUILD FAILURE — UHT / HEADER PARSE FAILED — Unreal Header Tool rejected the reflected declarations (a reflection/met
adata error, NOT a C++ compile error). Fix UENUM/USTRUCT/UCLASS annotations with Engineering.                         (exact command + diagnostics; also persisted in /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DI
AGNOSTIC_20261122T113635Z.log)                                                                                       ================================================================
Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/
mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64   
---- classification ----
  UHT / HEADER PARSE FAILED — Unreal Header Tool rejected the reflected declarations (a reflection/metadata error, NO
T a C++ compile error). Fix UENUM/USTRUCT/UCLASS annotations with Engineering.                                       
---- UHT activity (did UHT run?) ----
  UHT-related lines in build output: 5 (UHT was invoked/mentioned by UBT)
196:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:                                                       204:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:                                                        209:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:                                                         214:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:                                                        219:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:                                                
---- underlying exception / error detail (full capture, not tail) ----
24:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameM
ode.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found                                                31:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h
:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions                              34:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.
cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                  41:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.
cpp:50:36: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?  51:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem
.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            54:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem
.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                 57:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyste
m.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                79:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: st
atic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.106:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyst
em.cpp:24:12: error: no type named 'Tick' in 'UWorldSubsystem'                                                       109:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyst
em.cpp:24:17: error: declaration shadows a local variable [-Werror,-Wshadow]                                         130:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: s
tatic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.                                                                                                                    160:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry
.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            163:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                170:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:25:18: error: indirection requires pointer operand ('FName' invalid)                                           173:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:27:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?180:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:28:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?187:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:77:13: error: invalid argument type 'FSetElementId' to unary expression                                        197:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           200:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                205:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry
.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            210:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.
h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions                             215:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem
.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            220:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    225:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/TDDAdannaProxyCharacter.cp
p:198:50: error: no matching constructor for initialization of 'TActorIterator<ATDDForbiddenForestLevel>'            242:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:126:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                    248:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:126:119: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                        254:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:127:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                    260:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:127:120: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                        269:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    273:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           276:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                279:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.
cpp:83:26: error: no viable conversion from 'const FTDDActiveTierCounts' to 'const TDDWorld::FActiveTierCounts'      291:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.
cpp:118:53: error: no member named 'ToString' in 'FString'                                                           296:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDPopulationActor
.cpp:51:30: error: no member named 'GetRandInteger' in 'FMath'                                                       302:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem
.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            305:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsyste
m.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                327:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: s
tatic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.                                                                                                                    357:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    360:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulation
Subsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?        367:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulation
Subsystem.cpp:36:40: error: no member named 'ValueOrDefault' in 'TMap<FName, int>'                                   
---- last 60 lines of build output ----
 BUILD FAILURE — UHT / HEADER PARSE FAILED — Unreal Header Tool rejected the reflected declarations (a reflection/met
adata error, NOT a C++ compile error). Fix UENUM/USTRUCT/UCLASS annotations with Engineering.                         (exact command + diagnostics; also persisted in /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DI
AGNOSTIC_20261122T113635Z.log)                                                                                       ================================================================
Exact build command:
  /Users/Shared/Epic\ Games/UE_5.8/Engine/Build/BatchFiles/Mac/Build.sh  TDD_GAME  Mac  Development  -project=/Users/
mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/TDD_GAME.uproject  -WaitMutex  -architecture=arm64   
---- classification ----
  UHT / HEADER PARSE FAILED — Unreal Header Tool rejected the reflected declarations (a reflection/metadata error, NO
T a C++ compile error). Fix UENUM/USTRUCT/UCLASS annotations with Engineering.                                       
---- UHT activity (did UHT run?) ----
  UHT-related lines in build output: 5 (UHT was invoked/mentioned by UBT)
196:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDCalendarSubsystem.gen.cpp:8:                                                       204:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDLocationRegistry.gen.cpp:8:                                                        209:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDMarketSubsystem.gen.cpp:8:                                                         214:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDWeatherSubsystem.gen.cpp:8:                                                        219:In file included from /Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Intermediate/Build/M
ac/UnrealGame/Inc/TDD_GAME/UHT/TDDWorldPopulationSubsystem.gen.cpp:8:                                                
---- underlying exception / error detail (full capture, not tail) ----
24:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyGameM
ode.cpp:4:10: fatal error: 'TDDAdannaProxyCharacter.h' file not found                                                31:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.h
:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions                              34:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.
cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                  41:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDMarketSubsystem.
cpp:50:36: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?  51:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem
.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            54:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsystem
.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                 57:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyste
m.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                79:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: st
atic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.106:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyst
em.cpp:24:12: error: no type named 'Tick' in 'UWorldSubsystem'                                                       109:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDCalendarSubsyst
em.cpp:24:17: error: declaration shadows a local variable [-Werror,-Wshadow]                                         130:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: s
tatic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.                                                                                                                    160:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry
.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            163:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:16:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                170:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:25:18: error: indirection requires pointer operand ('FName' invalid)                                           173:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:27:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?180:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:28:33: error: no member named 'ESettlementKind' in namespace 'TDDWorld'; did you mean simply 'ESettlementKind'?187:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDLocationRegistr
y.cpp:77:13: error: invalid argument type 'FSetElementId' to unary expression                                        197:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           200:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                205:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDLocationRegistry
.h:55:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            210:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDMarketSubsystem.
h:53:18: error: 'BeginPlay' marked 'override' but does not override any member functions                             215:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem
.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            220:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    225:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/TDDAdannaProxyCharacter.cp
p:198:50: error: no matching constructor for initialization of 'TActorIterator<ATDDForbiddenForestLevel>'            242:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:126:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                    248:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:126:119: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                        254:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:127:36: error: declaration shadows a variable in namespace '(anonymous)' [-Werror,-Wshadow]                    260:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDOmegaValleyLeve
l.cpp:127:120: error: reference to type 'const FLinearColor' could not bind to an lvalue of type 'UInstancedStaticMeshComponent *'                                                                                                        269:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    273:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:19:18: error: 'BeginPlay' marked 'override' but does not override any member functions                           276:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDCalendarSubsyste
m.h:20:18: error: 'Tick' marked 'override' but does not override any member functions                                279:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.
cpp:83:26: error: no viable conversion from 'const FTDDActiveTierCounts' to 'const TDDWorld::FActiveTierCounts'      291:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDSettlementZone.
cpp:118:53: error: no member named 'ToString' in 'FString'                                                           296:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDPopulationActor
.cpp:51:30: error: no member named 'GetRandInteger' in 'FMath'                                                       302:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWeatherSubsystem
.h:51:18: error: 'BeginPlay' marked 'override' but does not override any member functions                            305:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWeatherSubsyste
m.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?                327:/Users/Shared/Epic Games/UE_5.8/Engine/Source/Runtime/Core/Public/String/FormatStringSanErrors.inl:15:1: error: s
tatic assertion failed due to requirement '(UE::Core::Private::FormatStringSan::EFormatStringSanStatus)7 != EFormatStringSanStatus::SNeedsWideCharPtrArgButGotNarrow': '%s' expects `TCHAR*` but got `ANSICHAR*` or `UTF8CHAR*`; use '%hs'.                                                                                                                    357:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Public/TDDWorldPopulationS
ubsystem.h:46:18: error: 'BeginPlay' marked 'override' but does not override any member functions                    360:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulation
Subsystem.cpp:14:5: error: no member named 'BeginPlay' in 'UWorldSubsystem'; did you mean simply 'BeginPlay'?        367:/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/ue_project/Source/TDD_GAME/Private/TDDWorldPopulation
Subsystem.cpp:36:40: error: no member named 'ValueOrDefault' in 'TMap<FName, int>'                                   
---- last 60 lines of build output ----

[diag] ACTION: send the full log (/Users/mhoodpc/TDD/TDD_PHASE3_PRODUCTION/PLAYABLE_ADANNA_M1/BUILD_DIAGNOSTIC_202611
22T113635Z.log) to Engineering. Do NOT fix C++ yourself.                                                             [diag] Engineering owns all Phase-1 C++ fixes. Phase 1 remains IMPLEMENTED_UNVERIFIED.
