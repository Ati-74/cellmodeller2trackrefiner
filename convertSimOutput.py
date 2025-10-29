import sys
from simOutputProcessing.scripts.cellModellerProcessing import process_simulation_directory


if __name__ == '__main__':

    # Path to the directory containing CellModeller `.pickle` files
    input_dir = "../input/cell modeller data"

    # If True, infer and assign cell types to tracked bacteria.
    assign_cell_type = True

    # Dictionary mapping cell type names to CellModeller IDs.
    cell_type_mapping = {'YFP': 0}

    # If True, approximates the parent bacterium by selecting the nearest disappeared bacterium from
    # the previous time step. Useful when large time step gaps cause the actual parent to no longer appear in
    # the previous step.
    use_grandmother_as_parent = False

    # Computes neighbor relationships between bacteria based on spatial proximity.
    # Two bacteria are considered neighbors if their expanded pixel boundaries touch.
    # This is consistent with CellProfiler's "MeasureObjectNeighbors" module.
    find_neighbors = True

    # Path to save output CSV files.
    output_dir = "../output/"

    # If the unit of length and the center coordinates of the bacteria are in µm, you need to pass this variable
    # to convert them into pixels, ensuring that the output is suitable for use as input in TrackRefiner.
    pixel_per_micron = 0.144

    # If True, converts CellModeller orientation angles into CellProfiler’s AreaShape_Orientation convention.
    cellprofiler_orientation_format = True

    # Start Processing
    process_simulation_directory(input_directory=input_dir, cell_type_mapping=cell_type_mapping,
                                 output_directory=output_dir, assign_cell_type=assign_cell_type,
                                 use_grandmother_as_parent=use_grandmother_as_parent,
                                 find_neighbors=find_neighbors, pixel_per_micron=pixel_per_micron,
                                 cellprofiler_orientation_format=cellprofiler_orientation_format)
