import dagger
from dagger import dag, function, object_type


@object_type
class KitopsHuggingfaceDagger:
    @function
    def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    @function
    async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
        """Returns lines that match a pattern in the files of the provided Directory"""
        return await (
            dag.container()
            .from_("alpine:latest")
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_exec(["grep", "-R", pattern, "."])
            .stdout()
        )
    
    @function
    def download_file_from_huggingface(hfrepo: str, path: str, secret: dagger.Secret) -> dagger.File:
        return (
            dag.huggingface()
            .download_file(hfrepo, path, secret)
        )
    
    @function
    def kit() -> dag.Kit:
        return (
            dag.kit()
        )

    @function
    async def version() -> str:
        return await (
            dag.kit()
            .version()
        )

    @function
    async def registry() -> str:
        return await (
            dag.kit()
            .registry()
        )

    @function
    def auth(username: str, password: dagger.Secret) -> dag.Kit:
        return (
            dag.kit()
            .with_auth(username, password)
        )

    @function
    def pack(directory: dagger.Directory, reference: str) -> dag.Kit:
        return (
            dag.kit()
            .pack(directory, reference)
        )
    
    @function
    def tag(current_ref: str, new_ref: str) -> dag.Kit:
        return (
            dag.kit()
            .tag(current_ref, new_ref)
        )

    @function
    async def push(reference: str) -> None:
        return await (
            dag.kit()
            .push(reference)
        )

