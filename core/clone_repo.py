from git import Repo
import shutil
import os
import stat


def remove_readonly(func, path, _):
    """
    Clear readonly flag and retry deletion
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clone_repository(repo_url, target_dir="temp_repo"):

    # Remove old repo safely
    if os.path.exists(target_dir):

        shutil.rmtree(
            target_dir,
            onerror=remove_readonly
        )

    # Clone fresh repository
    Repo.clone_from(repo_url, target_dir)

    return target_dir