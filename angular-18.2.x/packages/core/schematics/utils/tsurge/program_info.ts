/**
 * @license
 * Copyright Google LLC All Rights Reserved.
 *
 * Use of this source code is governed by an MIT-style license that can be
 * found in the LICENSE file at https://angular.dev/license
 */

import {NgtscProgram} from '../../../../compiler-cli/src/ngtsc/program';
import {NgCompilerOptions} from '../../../../compiler-cli/src/ngtsc/core/api';

import ts from 'typescript';
import {NgCompiler} from '../../../../compiler-cli/src/ngtsc/core';

/**
 * Base information for a TypeScript project, including an instantiated
 * TypeScript program. Base information may be extended by user-overridden
 * migration preparation methods to extend the stages with more data.
 */
export interface BaseProgramInfo {
  ngCompiler: NgCompiler | null;
  program: ts.Program;
  userOptions: NgCompilerOptions;
  programAbsoluteRootPaths: string[];
  tsconfigAbsolutePath: string;
}

/**
 * Full program information for a TypeScript project. This is the default "extension"
 * of the {@link BaseProgramInfo} with additional commonly accessed information.
 *
 * A different interface may be used as full program information, configured via a
 * {@link TsurgeMigration.prepareProgram} override.
 */
export interface ProgramInfo extends BaseProgramInfo {
  sourceFiles: ts.SourceFile[];
  fullProgramSourceFiles: readonly ts.SourceFile[];
  projectDirAbsPath: string;
}
